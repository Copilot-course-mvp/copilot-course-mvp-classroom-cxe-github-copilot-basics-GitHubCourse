# Step 04 — Test Generation

## Objective

Use Copilot to generate meaningful unit tests for edge-case-heavy logic.

## Copilot Feature Focus

- Test generation via chat/inline suggestions

## Task

1. Review `exercise.py`.
2. Create `student_tests.py` with `unittest` tests for `sanitize_tags`.
3. Include at least 6 assertions and cover edge cases.

Edge cases to include:

- Empty input
- Duplicate tags with mixed case
- Tags containing punctuation

## Example Prompts to Try

- "Generate Python unittest cases for this function including edge cases."
- "Add tests for empty input, duplicates, punctuation, and whitespace."

## Expected Behavior

- Tests are deterministic and readable.
- `sanitize_tags` behavior is verified, not reimplemented in tests.

## Validate

```bash
python3 scripts/evaluate.py --step step-04
```
