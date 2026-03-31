# GitHub Copilot Hands-On Course

An interactive, step-by-step training repository for practicing major GitHub Copilot capabilities in real code.

## Learning Objectives

By the end of this course, students will be able to use Copilot for:

- Code completion
- Chat flows (`/explain`, `/fix`, `/generate`)
- Refactoring support
- Test generation
- Documentation generation
- Code translation
- Debugging assistance

## Repository Structure

```text
.
├── step-01-code-completion/
├── step-02-chat-explain-fix-generate/
├── step-03-refactor/
├── step-04-test-generation/
├── step-05-documentation-generation/
├── step-06-code-translation/
├── step-07-debugging-assistance/
├── tests/
├── scripts/
└── .github/workflows/evaluate.yml
```

Each step folder contains:

- `README.md` with objective, instructions, prompts, and expected behavior
- Starter code students must complete
- `copilot-evidence.md` template for recording prompts/responses

## Quick Start

> **First time on macOS?** Follow the [SSH Credentials Setup Guide](SSH_SETUP_MAC.md) to generate your SSH key and add it to GitHub before cloning.

1. Clone repository (SSH) and open in VS Code.

   ```bash
   git clone git@github.com:josevicenteayala/GitHubCourse.git
   ```
2. Ensure Python 3.10+ is available.
3. Run all checks:

```bash
python3 scripts/evaluate.py
```

Run one step only:

```bash
python3 scripts/evaluate.py --step step-02
```

## How Students Use Copilot Here

- Use inline suggestions for implementation tasks.
- Use Copilot Chat for commands like `/explain`, `/fix`, `/generate` where specified.
- Save prompt evidence in each step’s `copilot-evidence.md`.
- Re-run evaluation script after each task for immediate feedback.

## Automated Evaluation Model

Evaluation uses two channels:

1. **Functional correctness**
	- `unittest` test cases under `tests/`
2. **Copilot usage evidence**
	- `scripts/evaluate.py` validates that each step’s `copilot-evidence.md` is filled and contains required command/prompt markers.

This keeps scoring objective while still checking that students actively used the intended Copilot feature.

## Agent Integration

`scripts/evaluate.py` acts as a deterministic reviewer agent:

- Loads step requirements
- Runs targeted tests and static checks
- Checks Copilot evidence artifacts
- Returns actionable pass/fail output per step

In CI, the same script runs via GitHub Actions for consistent feedback locally and remotely.

## Suggested Tech Stack

- Language: Python 3 (standard library)
- Testing: `unittest`
- Static checks: simple AST/text validators inside `scripts/evaluate.py`
- Automation: GitHub Actions

## Extension Ideas

- Add scoring (`points.json`) and leaderboard output.
- Add advanced steps for multi-file refactors.
- Add timed challenge mode with hidden tests.
- Add optional language tracks (TypeScript, Java).