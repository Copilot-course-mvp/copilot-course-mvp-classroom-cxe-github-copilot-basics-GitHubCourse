# Step 02 — Chat: /explain, /fix, /generate

## Copilot Feature
Chat commands: `/explain`, `/fix`, `/generate`

## Criteria
1. `parse_scoreboard(raw: str) -> dict` is fixed:
   - Handles spaces around separators
   - Ignores malformed segments (missing colon, non-numeric score)
   - Keeps the maximum score when a player appears multiple times
2. `top_player(scores: dict) -> tuple | None` is generated:
   - Returns `(name, score)` tuple for the highest scorer
   - Returns `None` for empty input
3. Code preserves original function signatures.
4. `copilot-evidence.md` contains evidence of using `/explain`, `/fix`, and `/generate` commands with real prompts and explanations.
