#!/usr/bin/env python3
"""AI Review Agent — reads step-specific prompts, sends diff to an LLM,
and posts structured feedback as a PR comment.

Usage:
    python3 scripts/agent_reviewer.py <diff_file> <step_id> <pr_number> <repo>

Environment variables:
    MODELS_API_KEY  — API key for GitHub Models (or compatible endpoint)
    GH_TOKEN        — GitHub token for posting comments (fallback: GITHUB_TOKEN)
"""
import os
import sys
import urllib.error
from pathlib import Path

from openai import OpenAI
import openai

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / ".github" / "prompts"

DEFAULT_MODEL = "gpt-5.4-mini"
VEREDICT_MODEL = "gpt-5.4-nano"  # can be different from review model if desired
MAX_DIFF_CHARS = 60_000  # truncate very large diffs to stay within context


def load_prompt(step_id: str) -> str:
    """Load and concatenate base prompt + step-specific prompt."""
    base_path = PROMPTS_DIR / "base-prompt.md"
    step_path = PROMPTS_DIR / f"{step_id}.md"

    parts: list[str] = []
    if base_path.exists():
        parts.append(base_path.read_text(encoding="utf-8"))
    else:
        print(f"Warning: {base_path} not found", file=sys.stderr)

    if step_path.exists():
        parts.append(step_path.read_text(encoding="utf-8"))
    else:
        print(f"Warning: {step_path} not found, using base prompt only", file=sys.stderr)

    return "\n\n---\n\n".join(parts)


def call_llm(system_prompt: str, diff_content: str, eval_output: str = "") -> str:
    """Send the prompt + diff to the LLM and return the response text."""
    api_key = os.environ.get("MODELS_API_KEY", "")
    if not api_key:
        raise RuntimeError("MODELS_API_KEY environment variable is not set")

    # Truncate diff if too large
    if len(diff_content) > MAX_DIFF_CHARS:
        diff_content = diff_content[:MAX_DIFF_CHARS] + "\n\n... (diff truncated)"

    client = OpenAI(api_key=api_key)

    user_message = f"Review the following code diff:\n\n```diff\n{diff_content}\n```"
    if eval_output:
        user_message += (
            f"\n\n---\n\n"
            f"The automated test suite produced the following evaluation output:\n\n"
            f"```\n{eval_output}\n```\n\n"
            f"Use this context to inform your review."
        )

    response = client.responses.create(
        model=DEFAULT_MODEL,
        instructions=system_prompt,
        input=user_message,
        temperature=0.3,
        max_output_tokens=2000,
    )

    print(f"LLM response received (id: {response.id}, model: {response.model})")
    print(f"Response content:\n{response.output_text}")
    return response.output_text


def classify_review(review_text: str) -> str:
    """Make a second LLM call to classify the review as PASS or FAIL."""
    api_key = os.environ.get("MODELS_API_KEY", "")
    if not api_key:
        raise RuntimeError("MODELS_API_KEY environment variable is not set")

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=VEREDICT_MODEL,
        instructions=(
            "You are a strict classifier. Given a code review of a student's pull request, "
            "determine whether the student's code meets ALL the criteria. "
            "Respond with exactly one word: PASS or FAIL. Nothing else."
        ),
        input=f"Classify this code review:\n\n{review_text}",
        temperature=0.0,
        max_output_tokens=16,
    )

    verdict = response.output_text.strip().upper()
    print(f"Classification response: {verdict}")
    if verdict not in ("PASS", "FAIL"):
        print(f"Unexpected classification response: {response.output_text!r}, defaulting to FAIL", file=sys.stderr)
        return "FAIL"
    return verdict


def post_review_comment(repo: str, pr_number: str, body: str) -> None:
    """Post the AI review as a PR comment via post_comment.py logic."""
    # Import the sibling module
    scripts_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(scripts_dir))
    from post_comment import post_or_update

    post_or_update(repo, int(pr_number), "ai-review-agent", body)


def main() -> int:
    if len(sys.argv) != 5:
        print(
            "Usage: agent_reviewer.py <diff_file> <step_id> <pr_number> <repo>",
            file=sys.stderr,
        )
        return 1

    diff_file, step_id, pr_number, repo = sys.argv[1:5]

    diff_path = Path(diff_file)
    if not diff_path.exists():
        print(f"Diff file not found: {diff_file}", file=sys.stderr)
        return 1

    diff_content = diff_path.read_text(encoding="utf-8", errors="replace")
    if not diff_content.strip():
        print("Diff is empty, skipping AI review")
        return 0

    system_prompt = load_prompt(step_id)
    eval_output = os.environ.get("EVAL_OUTPUT", "")

    try:
        review = call_llm(system_prompt, diff_content, eval_output)
    except RuntimeError as exc:
        print(f"Skipping AI review: {exc}", file=sys.stderr)
        return 0
    except openai.APIError as exc:
        print(f"LLM API error: {exc.status_code} {exc.message}", file=sys.stderr)
        return 0

    # Classify the review as PASS or FAIL via a second LLM call
    try:
        verdict = classify_review(review)
    except (RuntimeError, openai.APIError) as exc:
        print(f"Classification failed ({exc}), defaulting to FAIL", file=sys.stderr)
        verdict = "FAIL"

    verdict_badge = "✅ PASS" if verdict == "PASS" else "❌ FAIL"
    comment_body = (
        f"🤖 **AI Review for `{step_id}`**\n\n"
        f"{review}\n\n---\n\n**Verdict: {verdict_badge}**"
    )

    try:
        post_review_comment(repo, pr_number, comment_body)
    except urllib.error.HTTPError as exc:
        print(f"Failed to post comment: {exc.code} {exc.reason}", file=sys.stderr)
        body = exc.read().decode()
        print(body, file=sys.stderr)
        return 1

    # Output verdict for workflow consumption
    print(f"VERDICT={verdict}")

    # Exit code: 0 = PASS, 2 = FAIL (distinct from 1 = error)
    return 0 if verdict == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
