# Step 01 — Code Completion

## Objective

Use Copilot inline code completion to implement two small utility functions quickly and correctly.

## Copilot Feature Focus

- Inline code completion

## Task

Edit `exercise.py` and implement:

1. `normalize_username(name: str) -> str`
2. `build_slug(title: str) -> str`

Rules are documented in function docstrings.

## Example Prompts to Try

- "Complete this function to normalize usernames."
- "Generate a robust slugify helper for lowercase ASCII and hyphens."

## Expected Behavior

- Usernames are lowercase, trimmed, and only `[a-z0-9_]` remain.
- Slugs are lowercase words separated by single `-`, with punctuation removed.

## Validate

```bash
python3 scripts/evaluate.py --step step-01
```