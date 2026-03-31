## Step 7: Debugging Assistance — Diagnose and Fix Logic Defects

One step to go! 🎉 In this final step you will use Copilot's debugging features to identify and fix multiple bugs in an existing function.

### 📖 Theory: Debugging with Copilot

Copilot can act as a pair programmer for debugging by:

- **Explaining** why a function fails for specific inputs.
- **Suggesting fixes** via `/fix` that preserve the original API contract.
- **Walking through** the logic step-by-step when asked.

Always verify the suggested fix with your own unit tests before committing.

### ⌨️ Activity: Fix `summarize_response_times`

1. Open `step-07-debugging-assistance/exercise.py`. The function `summarize_response_times` is supposed to:
   - Accept a list of integer/float response times.
   - Ignore negative values.
   - Return `{"min": ..., "max": ..., "avg": ...}` as floats.
   - Return `{"min": 0.0, "max": 0.0, "avg": 0.0}` for empty or all-negative input.

   But it contains several bugs.

2. Select the function and ask Copilot to explain the failures:

   > **Prompt to try:**
   > ```text
   > Why does this function fail for empty input and for lists containing only negative values?
   > ```

   Record the explanation in `copilot-evidence.md`.

3. Fix the function with Copilot's help:

   > **Prompt to try:**
   > ```text
   > /fix this function to correctly handle empty input and negative values while preserving the {"min", "max", "avg"} output schema
   > ```

4. Save and validate:

   ```bash
   python3 scripts/evaluate.py --step step-07
   ```

5. Fill in `step-07-debugging-assistance/copilot-evidence.md` with your debug prompt, the `/fix` prompt, and the corrected code.

6. Open a pull request targeting `main` with your changes to `step-07-debugging-assistance/` to trigger the final automated evaluation.

<details>
<summary>Having trouble? 🤷</summary>

- Run `python3 -m unittest tests.test_step07 -v` locally to see the exact failure messages.
- Make sure the function returns plain Python `float` values (not `int`).
- After fixing, run `python3 scripts/evaluate.py` (no `--step` flag) to see the full course summary.

</details>
