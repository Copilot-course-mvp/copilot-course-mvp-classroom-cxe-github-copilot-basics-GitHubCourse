# Step 04 — Test Generation

## Copilot Feature
Test generation via chat/inline suggestions

## Criteria
1. `student_tests.py` exists in `step-04-test-generation/`.
2. Contains at least 6 assertions (`self.assert*` calls).
3. Tests cover the required edge cases:
   - Empty input
   - Duplicate tags with mixed case
   - Tags containing punctuation
4. Tests are deterministic and readable — they verify behavior, not reimplement the function.
5. All student-written tests pass when run.
6. `copilot-evidence.md` contains the word "test" and describes the test generation process.
