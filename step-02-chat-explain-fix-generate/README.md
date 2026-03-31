# Step 02 — Chat: /explain, /fix, /generate

## Objective

Use Copilot Chat to understand buggy logic, fix it, and generate one helper function.

## Copilot Feature Focus

- `/explain`
- `/fix`
- `/generate`

## Task

1. Open `exercise.py`.
2. Run `/explain` on `parse_scoreboard` and summarize what is wrong.
3. Use `/fix` to correct parsing bugs.
4. Use `/generate` to create `top_player` helper.

## Example Prompts to Try

- `/explain this function and list failure cases`
- `/fix this function but keep the same signature`
- `/generate a helper that returns the player with max score`

## Expected Behavior

- Handles spaces around separators.
- Ignores malformed segments.
- Keeps the maximum score for repeated players.
- `top_player` returns `(name, score)` or `None` for empty input.

## Validate

```bash
python3 scripts/evaluate.py --step step-02
```