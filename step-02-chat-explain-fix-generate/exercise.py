def parse_scoreboard(raw: str) -> dict[str, int]:
    """Parse 'name:score' pairs separated by commas.

    Example: "alice:10,bob:9,alice:14" -> {"alice": 14, "bob": 9}

    Invalid segments should be skipped.
    """

    board: dict[str, int] = {}
    if raw == "":
        return board

    parts = raw.split(",")
    for part in parts:
        try:
            name, score = part.split(":", 1)
            name = name.lower()
            value = int(score)
            board[name] = value
        except ValueError:
            continue
    return board


def top_player(board: dict[str, int]) -> tuple[str, int] | None:
    """Return the player with the highest score, else None.

    Keep this deterministic by sorting names alphabetically when scores tie.
    """
    if not board:
        return None
    max_score = max(board.values())
    top_player_name = min(name for name, score in board.items() if score == max_score)
    return (top_player_name, max_score)