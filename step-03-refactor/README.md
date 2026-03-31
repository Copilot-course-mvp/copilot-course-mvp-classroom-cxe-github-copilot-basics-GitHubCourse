# Step 03 — Refactoring Suggestions

## Objective

Refactor repetitive logic with Copilot while preserving behavior.

## Copilot Feature Focus

- Chat-guided refactoring

## Task

In `exercise.py`, remove duplication by extracting shared discount logic.

Required constraints:

- Keep all public function signatures unchanged.
- Add a helper named `apply_discount`.
- `checkout_total` and `invoice_total` must use that helper.

## Example Prompts to Try

- "Refactor this file to remove duplicated discount logic."
- "Extract a helper and keep behavior exactly the same."

## Expected Behavior

- Totals are unchanged for existing valid inputs.
- Edge cases still work (`[]`, discount `0`, discount `100`).

## Validate

```bash
python3 scripts/evaluate.py --step step-03
```
