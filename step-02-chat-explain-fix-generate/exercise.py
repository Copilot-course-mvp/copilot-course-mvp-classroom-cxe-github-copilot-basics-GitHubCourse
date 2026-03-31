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
        if ":" not in part:
            continue
        name, score = part.split(":", 1)
        name = name.strip().lower()
        score = score.strip()
        try:
            value = int(score)
        except ValueError:
            continue
        if name in board:
            board[name] = max(board[name], value)
        else:
            board[name] = value
    return board


def top_player(board: dict[str, int]) -> tuple[str, int] | None:
    """Return the player with the highest score, else None.

    Keep this deterministic by sorting names alphabetically when scores tie.
    """
    if not board:
        return None
    return min(board.items(), key=lambda item: (-item[1], item[0]))