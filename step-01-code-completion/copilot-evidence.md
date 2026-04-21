
# Copilot Evidence — Step 01

Completion of normalize_username and build_slug functions using GitHub Copilot inline code completion.

## Prompt 1

"Let's build 2 small functions in Python to normalize username strings and create URL-friendly slugs."

### Function 1: normalize_username
Rules:
- Trim outer whitespace
- Convert to lowercase
- Replace spaces with underscores
- Remove any character that is not a-z, 0-9, or underscore
- Collapse repeated underscores into one underscore
- Strip leading/trailing underscores

### Function 2: build_slug
Rules:
- Lowercase
- Keep letters and digits
- Replace any sequence of non-alphanumeric characters with a single '-'
- Strip leading/trailing '-'

## Copilot Suggestion

Copilot provided the following implementation using regex patterns:

```python
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
```

## Why I Accepted This Suggestion

The implementation is clear, efficient, and follows all the specified rules:
- Uses regex patterns appropriately for string transformations
- Each line is well-commented explaining the purpose
- The logic is straightforward and easy to understand
- Handles all edge cases mentioned in the requirements
- Uses Python standard library (re module) without unnecessary dependencies

## Final Observations

The suggestion demonstrates good coding practices:
- Proper use of regex anchors and character classes
- Sequential transformations for clarity
- Comments explaining each step
- Correct use of string methods (strip, lower)
- Efficient handling of whitespace and character filtering
