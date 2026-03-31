## Step 4: Test Generation — Write Edge-Case Tests with Copilot

Refactoring done — well done! 🎉 Now let's use Copilot to generate meaningful unit tests for a function full of edge cases.

### 📖 Theory: Test Generation with Copilot

Copilot excels at writing test cases when you give it:

- The function under test (select it or paste it into chat).
- A list of edge-case categories you care about.
- The testing framework you are using (`unittest`, `pytest`, etc.).

The more specific your prompt, the more useful the generated tests will be.

### ⌨️ Activity: Generate Tests for `sanitize_tags`

1. Open `step-04-test-generation/exercise.py` and read `sanitize_tags`. It:
   - Accepts a list of raw tag strings.
   - Strips whitespace from each tag.
   - Removes punctuation.
   - Lowercases everything.
   - Deduplicates (case-insensitively).
   - Returns a sorted list.

2. Create `step-04-test-generation/student_tests.py`. You can start with Copilot:

   > **Prompt to try:**
   > ```text
   > Generate Python unittest test cases for the sanitize_tags function covering:
   > - empty input
   > - duplicate tags with mixed case
   > - tags containing punctuation
   > - tags with leading/trailing whitespace
   > Include at least 6 assertions total.
   > ```

3. Make sure your test file:
   - Has `import unittest` and a class inheriting from `unittest.TestCase`.
   - Covers **empty input**, **duplicate** tags, and **punctuation** (these words must appear in the file).
   - Contains **at least 6** `self.assert*` calls.
   - Passes when run: `python3 step-04-test-generation/student_tests.py`

4. Validate:

   ```bash
   python3 scripts/evaluate.py --step step-04
   ```

5. Fill in `step-04-test-generation/copilot-evidence.md` with the prompt you used and the generated test snippet.

6. Open a pull request targeting `main` with your changes to `step-04-test-generation/`.

<details>
<summary>Having trouble? 🤷</summary>

- The evaluator counts `self.assert` occurrences — make sure you have at least 6.
- The words "empty", "duplicate", and "punctuation" must appear somewhere in the file (e.g., in test method names or comments).
- Use `python3 step-04-test-generation/student_tests.py` to run the tests directly and see failure output.

</details>
