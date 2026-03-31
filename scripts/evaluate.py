#!/usr/bin/env python3
import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

# Sentinel strings that appear in evidence files when they are still in template
# (placeholder) state.  Defining them as constants makes maintenance easier.
_TEMPLATE_SENTINELS: tuple[str, ...] = (
    "replace all placeholders",
    "<paste",
    "<short note",
)


@dataclass(frozen=True)
class StepConfig:
    id: str
    folder: str
    test_modules: list[str]
    evidence_tokens: list[str]


STEPS: list[StepConfig] = [
    StepConfig(
        id="step-01",
        folder="step-01-code-completion",
        test_modules=["tests.test_step01"],
        evidence_tokens=["prompt"],
    ),
    StepConfig(
        id="step-02",
        folder="step-02-chat-explain-fix-generate",
        test_modules=["tests.test_step02"],
        evidence_tokens=["/explain", "/fix", "/generate"],
    ),
    StepConfig(
        id="step-03",
        folder="step-03-refactor",
        test_modules=["tests.test_step03"],
        evidence_tokens=["refactor"],
    ),
    StepConfig(
        id="step-04",
        folder="step-04-test-generation",
        test_modules=[],
        evidence_tokens=["test"],
    ),
    StepConfig(
        id="step-05",
        folder="step-05-documentation-generation",
        test_modules=["tests.test_step05"],
        evidence_tokens=["documentation"],
    ),
    StepConfig(
        id="step-06",
        folder="step-06-code-translation",
        test_modules=["tests.test_step06"],
        evidence_tokens=["translate"],
    ),
    StepConfig(
        id="step-07",
        folder="step-07-debugging-assistance",
        test_modules=["tests.test_step07"],
        evidence_tokens=["debug", "/fix"],
    ),
]


def run_unittest(module: str) -> tuple[bool, str]:
    command = [sys.executable, "-m", "unittest", module]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    output = (result.stdout + "\n" + result.stderr).strip()
    return result.returncode == 0, output


def check_evidence(config: StepConfig) -> tuple[bool, list[str]]:
    evidence_file = ROOT / config.folder / "copilot-evidence.md"
    if not evidence_file.exists():
        return False, ["Missing copilot-evidence.md"]

    content = evidence_file.read_text(encoding="utf-8").lower()
    failures: list[str] = []

    if any(sentinel in content for sentinel in _TEMPLATE_SENTINELS):
        failures.append("Evidence file still contains placeholders")

    for token in config.evidence_tokens:
        if token.lower() not in content:
            failures.append(f"Missing evidence token: {token}")

    return len(failures) == 0, failures


def check_step04_student_tests() -> tuple[bool, list[str]]:
    failures: list[str] = []
    test_file = ROOT / "step-04-test-generation" / "student_tests.py"
    if not test_file.exists():
        return False, ["Missing student_tests.py"]

    content = test_file.read_text(encoding="utf-8")
    assert_count = len(re.findall(r"self\.assert", content))
    if assert_count < 6:
        failures.append(f"Expected at least 6 assertions in student_tests.py, found {assert_count}")

    required_terms = ["empty", "duplicate", "punctuation"]
    lower_content = content.lower()
    for term in required_terms:
        if term not in lower_content:
            failures.append(f"Expected explicit test coverage hint for: {term}")

    result = subprocess.run(
        [sys.executable, str(test_file)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        failures.append("student_tests.py is failing")
        failures.append((result.stdout + "\n" + result.stderr).strip())

    return len(failures) == 0, failures


def evaluate_step(config: StepConfig) -> tuple[bool, list[str]]:
    messages: list[str] = []
    step_ok = True

    for module in config.test_modules:
        ok, output = run_unittest(module)
        if not ok:
            step_ok = False
            messages.append(f"Unit test failure in {module}")
            messages.append(output)

    if config.id == "step-04":
        ok, failures = check_step04_student_tests()
        if not ok:
            step_ok = False
            messages.extend(failures)

    evidence_ok, evidence_failures = check_evidence(config)
    if not evidence_ok:
        step_ok = False
        messages.extend(evidence_failures)

    if step_ok:
        messages.append("All checks passed")

    return step_ok, messages


def is_step_started(config: StepConfig) -> bool:
    """Return True if the student has started working on this step.

    A step is considered not started when the evidence file is still in its
    template state (contains the placeholder sentinels added by the course
    scaffolding).
    """
    evidence_file = ROOT / config.folder / "copilot-evidence.md"
    if not evidence_file.exists():
        return False

    content = evidence_file.read_text(encoding="utf-8").lower()
    return not any(sentinel in content for sentinel in _TEMPLATE_SENTINELS)


def detect_changed_steps() -> list[str] | None:
    """Detect which steps have changed files using git diff.

    Returns a list of step IDs that have both changed files (detected via
    ``git diff``) *and* have been started by the student (evidence file not
    in template state).  Returns ``None`` when the git diff itself fails so
    that the caller can fall back to a different strategy.
    """
    import os

    event_name = os.environ.get("GITHUB_EVENT_NAME", "push")
    base_ref = os.environ.get("GITHUB_BASE_REF", "")

    try:
        if event_name == "pull_request" and base_ref:
            cmd = ["git", "diff", "--name-only", f"origin/{base_ref}...HEAD"]
        else:
            cmd = ["git", "diff", "--name-only", "HEAD~1..HEAD"]

        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=True)
        changed_files = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]
    except subprocess.CalledProcessError:
        return None

    changed_step_ids = []
    for config in STEPS:
        if any(f.startswith(config.folder + "/") for f in changed_files):
            if is_step_started(config):
                changed_step_ids.append(config.id)

    return changed_step_ids


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate GitHub Copilot course steps")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--step",
        choices=[config.id for config in STEPS],
        help="Evaluate only one specific step",
    )
    group.add_argument(
        "--auto",
        action="store_true",
        help="Auto-detect which steps have changed using git diff and evaluate only those",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.auto:
        changed = detect_changed_steps()
        if changed is None:
            print("Warning: Could not detect changed steps via git, falling back to started-steps detection")
            targets = [config for config in STEPS if is_step_started(config)]
            if not targets:
                print("No started steps found, skipping evaluation")
                return 0
        elif not changed:
            print("No started step changes detected, skipping evaluation")
            return 0
        else:
            targets = [config for config in STEPS if config.id in changed]
    else:
        targets = [config for config in STEPS if not args.step or config.id == args.step]

    overall_ok = True
    print("== GitHub Copilot Course Evaluation ==")

    for config in targets:
        print(f"\n[{config.id}] {config.folder}")
        ok, messages = evaluate_step(config)
        status = "PASS" if ok else "FAIL"
        print(f"Status: {status}")
        for msg in messages:
            print(f"- {msg}")
        overall_ok = overall_ok and ok

    print("\nSummary:", "PASS" if overall_ok else "FAIL")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())