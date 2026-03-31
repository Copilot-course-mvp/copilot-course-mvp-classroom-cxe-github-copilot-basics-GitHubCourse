# Step 06 — Code Translation

## Objective

Use Copilot to translate JavaScript logic into idiomatic Python.

## Copilot Feature Focus

- Code translation

## Task

In `exercise.py`, implement `group_by_domain` in Python using behavior defined by the JavaScript reference.

## Example Prompts to Try

- "Translate this JavaScript function to Python preserving behavior and edge cases."
- "Rewrite this in idiomatic Python with type hints."

## Expected Behavior

- Email domains are case-insensitive.
- Invalid email strings are ignored.
- Output keys are sorted alphabetically.

## Validate

```bash
python3 scripts/evaluate.py --step step-06
```
