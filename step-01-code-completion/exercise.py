import re


def normalize_username(name: str) -> str:
    """Normalize a username.

    Rules:
    - Trim outer whitespace.
    - Convert to lowercase.
    - Replace spaces with underscores.
    - Remove any character that is not a-z, 0-9, or underscore.
    - Collapse repeated underscores into one underscore.
    - Strip leading/trailing underscores.
    """
    raise NotImplementedError("Implement with Copilot code completion")


def build_slug(title: str) -> str:
    """Convert a title into a URL-friendly slug.

    Rules:
    - Lowercase.
    - Keep letters and digits.
    - Replace any sequence of non-alphanumeric characters with a single '-'.
    - Strip leading/trailing '-'.
    """
    raise NotImplementedError("Implement with Copilot code completion")