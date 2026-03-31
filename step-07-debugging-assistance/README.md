# Step 07 — Debugging Assistance

## Objective

Use Copilot to diagnose and fix logic defects in an existing function.

## Copilot Feature Focus

- Debugging via chat assistance and `/fix`

## Task

`exercise.py` contains `summarize_response_times` with multiple bugs.

Use Copilot to:

1. Explain failures.
2. Suggest a fix.
3. Apply/refine the fix.

## Example Prompts to Try

- "Why does this function fail for empty input and outliers?"
- "/fix this function and preserve output schema"

## Expected Behavior

- Correctly computes min, max, and average.
- Ignores negative values.
- Handles empty/invalid input safely.

## Validate

```bash
python3 scripts/evaluate.py --step step-07
```
