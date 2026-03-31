# Copilot Instructions — GitHub Copilot Hands-On Course

This repository is an interactive training course that teaches students to use GitHub Copilot through seven practical exercises. Each step focuses on a different Copilot capability.

## When reviewing Pull Requests

- This is a **learning environment**. Students are expected to use Copilot to complete exercises. The goal is correct, idiomatic Python — not perfection.
- Each PR targets **one step** (identified by the branch name prefix or a PR label like `step-01`).
- Focus your review on:
  1. **Functional correctness** — Does the code meet the requirements in the step's README?
  2. **Idiomatic Python** — Are there simpler or more Pythonic ways to express the logic?
  3. **Edge cases** — Has the student handled boundary conditions described in the exercise?
  4. **Copilot evidence** — The `copilot-evidence.md` file should contain real prompts and genuine reflections, not placeholders.
- Be encouraging but precise. Point out issues with specific suggestions for improvement.
- Do not rewrite solutions for the student — guide them toward the fix.

## Step reference

| Step | Feature | Key criteria |
|------|---------|-------------|
| step-01 | Code completion | `normalize_username` and `build_slug` implemented correctly |
| step-02 | Chat /explain /fix /generate | `parse_scoreboard` fixed, `top_player` generated |
| step-03 | Refactoring | `apply_discount` helper extracted, no duplication |
| step-04 | Test generation | `student_tests.py` with ≥6 assertions, covers empty/duplicate/punctuation |
| step-05 | Documentation | Docstrings with purpose/params/return/example, USAGE.md filled |
| step-06 | Code translation | JS → idiomatic Python, case-insensitive domains, invalid emails ignored |
| step-07 | Debugging | Bugs in `summarize_response_times` identified and fixed |
