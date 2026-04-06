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
    s = name.strip().lower()
    # replace spaces with underscores
    s = s.replace(" ", "_")
    # remove any character that is not a-z, 0-9 or underscore
    s = re.sub(r"[^a-z0-9_]+", "", s)
    # collapse repeated underscores
    s = re.sub(r"_+", "_", s)
    return s.strip("_")


def build_slug(title: str) -> str:
    """Convert a title into a URL-friendly slug.

    Rules:
    - Lowercase.
    - Keep letters and digits.
    - Replace any sequence of non-alphanumeric characters with a single '-'.
    - Strip leading/trailing '-'.
    """
    s = title.lower()
    # replace any sequence of non a-z or 0-9 characters with a single '-'
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")