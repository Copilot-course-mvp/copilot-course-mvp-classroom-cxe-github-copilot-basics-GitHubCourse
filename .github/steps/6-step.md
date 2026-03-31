## Step 6: Code Translation — Port JavaScript Logic to Python

Docs done — excellent! 🎉 In this step you will use Copilot to **translate** an existing function from JavaScript into idiomatic Python.

### 📖 Theory: Code Translation with Copilot

Copilot can convert code between languages by understanding the intent rather than performing a mechanical token-by-token substitution. The best approach is to:

1. Paste the source-language snippet into Copilot Chat.
2. Ask it to translate to the target language while following idiomatic conventions.
3. Review the output for correctness and style.

### ⌨️ Activity: Implement `group_by_domain` in Python

1. Open `step-06-code-translation/exercise.py`. The file contains a function stub with a JavaScript reference implementation in the docstring comment.

2. Ask Copilot to translate it:

   > **Prompt to try:**
   > ```text
   > Translate the JavaScript implementation in the docstring into idiomatic Python.
   > - Strip whitespace from each email before processing.
   > - Normalize domains to lowercase.
   > - Skip any string that does not contain exactly one "@".
   > - Return a dict mapping each domain to its email count.
   > ```

3. Accept or refine the suggestion so that `group_by_domain` works correctly.

4. Save and validate:

   ```bash
   python3 scripts/evaluate.py --step step-06
   ```

5. Fill in `step-06-code-translation/copilot-evidence.md` with the prompt you used and the translated code snippet.

6. Open a pull request targeting `main` with your changes to `step-06-code-translation/`.

<details>
<summary>Having trouble? 🤷</summary>

- The test passes `["A@Example.com", "b@example.com", "bad-email", "c@other.org", "d@OTHER.ORG "]` and expects `{"example.com": 2, "other.org": 2}`.
- Make sure domain comparison is case-insensitive and that `"bad-email"` (no `@`) is skipped.
- Run `python3 scripts/evaluate.py --step step-06` locally for details.

</details>
