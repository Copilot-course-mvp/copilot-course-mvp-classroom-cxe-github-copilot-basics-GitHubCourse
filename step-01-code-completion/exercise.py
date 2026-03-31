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
    name = name.strip()
    name = name.lower()
    name = name.replace(' ', '_')
    name = re.sub(r'[^a-z0-9_]', '', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    return name
 

def build_slug(title: str) -> str:
    """Convert a title into a URL-friendly slug.

    Rules:
    - Lowercase.
    - Keep letters and digits.
    - Replace any sequence of non-alphanumeric characters with a single '-'.
    - Strip leading/trailing '-'.
    """
    title = title.strip()
    title = title.lower()
    title = re.sub(r'[^a-z0-9]+', '-', title)
    title = title.strip('-')
    return title

