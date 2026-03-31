# Copilot Evidence — Step 02

## /explain output summary

Used /explain on `parse_scoreboard` to understand the existing logic. Copilot explained it splits by comma, then by colon, and maps names to scores, but noted it doesn't handle malformed input or keep maximum scores.

## /fix prompt used

Used /fix to add error handling: strip whitespace from name/score, skip segments without colon, wrap int conversion in try/except, and keep the maximum score for duplicate players.

## /generate prompt used

Used /generate to implement `top_player`. Prompt: "Generate a function that returns the player with the highest score as a tuple, alphabetically first on tie, or None if empty."

## What you changed manually afterward

Verified the fix handles all edge cases including missing colons, non-integer scores, and spaces around separators.
