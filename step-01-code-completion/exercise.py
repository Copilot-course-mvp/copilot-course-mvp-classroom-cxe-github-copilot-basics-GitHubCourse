import re
def normalize_username(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r'\s+', '_', name)  # Replace spaces with underscores
    name = re.sub(r'[^a-z0-9_]', '', name)  # Remove invalid characters
    name = re.sub(r'_{2,}', '_', name)  # Collapse repeated underscores
    return name.strip('_')  # Strip leading/trailing underscores

def build_slug(title: str) -> str:
    title = title.lower()
    title = re.sub(r'[^a-z0-9]+', '-', title)  # Replace non-alphanumeric with '-'
    return title.strip('-')  # Strip leading/trailing '-'

