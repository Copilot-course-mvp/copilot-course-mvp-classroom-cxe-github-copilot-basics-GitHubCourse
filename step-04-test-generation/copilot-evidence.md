# Copilot Evidence — Step 04

## Prompt used for test generation

Asked Copilot to generate unit tests for the `sanitize_tags` function covering edge cases: empty input, duplicate removal, punctuation handling, hyphen preservation, and whitespace trimming.

## Extra edge case Copilot missed

Added a test for tags that become empty after punctuation removal (e.g., "!!!", "...", "@@@") to ensure they are properly discarded rather than kept as empty strings.

## Final test count

8 test methods with 8 assertions total, covering: basic lowercase/trim, empty tags, duplicate removal, punctuation stripping, hyphen preservation, empty list, all-invalid tags, and post-normalization duplicates.
