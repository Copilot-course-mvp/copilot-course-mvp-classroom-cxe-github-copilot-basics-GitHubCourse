# Step 01 — Code Completion

## Copilot Feature
Inline code completion

## Criteria
1. `normalize_username(name: str) -> str` is implemented with all documented rules:
	- trim outer whitespace
	- lowercase output
	- collapse whitespace (including tabs/newlines) to `_`
	- remove characters outside `[a-z0-9_]`
	- collapse repeated underscores and strip leading/trailing underscores
2. `build_slug(title: str) -> str` is implemented with all documented rules:
	- lowercase output
	- keep only alphanumeric word segments
	- convert runs of non-alphanumeric characters to a single `-`
	- strip leading/trailing `-`
3. Edge cases are handled:
	- inputs that normalize to empty strings (for example `"!!!"`, `"***"`, or only underscores)
	- multiple separators/punctuation sequences
	- mixed spacing patterns such as consecutive spaces, tabs, and newlines
4. Type safety is explicit:
	- `normalize_username` raises `TypeError("name must be a string")` for non-string input
	- `build_slug` raises `TypeError("title must be a string")` for non-string input
5. Code remains clean and Pythonic (for example, appropriate `re` usage and straightforward transformations).
