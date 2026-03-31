## Step 1: Code Completion — Implement Utility Functions

Welcome to the GitHub Copilot Hands-On Course, @{{login}}! 🎉

In this first step you will use Copilot's **inline code completion** to implement two small utility functions. This is the most fundamental Copilot feature: as you type, Copilot predicts and offers completions for the rest of your code.

### 📖 Theory: Inline Code Completion

GitHub Copilot watches your code context (file content, docstrings, function signatures) and suggests completions in real time. To get the best results:

- Write a clear function signature and docstring **before** accepting a suggestion.
- Use `Tab` to accept a suggestion, or `Esc` to dismiss it.
- If the first suggestion isn't right, press `Alt+]` (or `Option+]` on Mac) to cycle through alternatives.

### ⌨️ Activity: Implement `normalize_username` and `build_slug`

1. Open `step-01-code-completion/exercise.py` in VS Code.

2. Read the docstring for `normalize_username`. It describes the exact transformation rules:
   - Trim outer whitespace
   - Lowercase
   - Replace spaces with underscores
   - Remove any character that is not `a-z`, `0-9`, or `_`
   - Collapse repeated underscores
   - Strip leading/trailing underscores

3. Delete the `raise NotImplementedError(...)` line and start typing the implementation. Let Copilot complete it.

   > **Prompt to try:**
   > ```text
   > Complete this function to normalize usernames following the rules in the docstring.
   > ```

4. Do the same for `build_slug`. Rules: lowercase, keep letters and digits, replace any sequence of non-alphanumeric characters with a single `-`, strip leading/trailing `-`.

5. Save the file and validate:

   ```bash
   python3 scripts/evaluate.py --step step-01
   ```

6. Fill in `step-01-code-completion/copilot-evidence.md` with the prompts you used and Copilot's responses.

7. Open a pull request targeting `main` with your changes to `step-01-code-completion/` to trigger automated evaluation.

<details>
<summary>Having trouble? 🤷</summary>

- Make sure you have the GitHub Copilot extension installed and signed in.
- If Copilot is not suggesting anything, try adding more context above the function (e.g., an example in the docstring).
- Run `python3 scripts/evaluate.py --step step-01` locally to see detailed failure messages.

</details>
