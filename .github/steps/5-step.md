## Step 5: Documentation Generation — Add Docstrings and a USAGE Guide

Tests passing — amazing! 🎉 In this step you will use Copilot to generate docstrings and a usage guide for two utility functions.

### 📖 Theory: Documentation Generation with Copilot

Copilot can generate structured docstrings when you:

- Position the cursor just inside the function body after the `def` line.
- Type `"""` and wait — Copilot will suggest a full docstring.
- Or use Copilot Chat: select the function and prompt `/generate a Google-style docstring`.

Well-written docstrings include **Args/Parameters**, **Returns**, and often **Raises** and **Examples** sections.

### ⌨️ Activity: Document `chunk_list` and `moving_average`

1. Open `step-05-documentation-generation/exercise.py`. Both functions are implemented but lack docstrings.

2. For each function, generate a docstring with Copilot:

   > **Prompt to try:**
   > ```text
   > /generate a NumPy-style docstring for this function including Parameters and Returns sections
   > ```

   Make sure the docstring includes the words **Parameters** and **Returns** — the test checks for them.

3. Open (or create) `step-05-documentation-generation/USAGE.md`. Copilot can draft it:

   > **Prompt to try:**
   > ```text
   > Generate a USAGE.md for chunk_list and moving_average: include a brief description, parameter table, return value, and two code examples for each function.
   > ```

   Remove any `TODO` placeholders from the file — the test checks that none remain.

4. Save and validate:

   ```bash
   python3 scripts/evaluate.py --step step-05
   ```

5. Fill in `step-05-documentation-generation/copilot-evidence.md` with the prompts and a short note on the documentation generated.

6. Open a pull request targeting `main` with your changes to `step-05-documentation-generation/`.

<details>
<summary>Having trouble? 🤷</summary>

- The test checks `__doc__` for the strings "Parameters" and "Returns" (case-sensitive).
- Ensure `USAGE.md` exists in the `step-05-documentation-generation/` folder and contains no `TODO`.
- Run `python3 scripts/evaluate.py --step step-05` locally for detailed failure messages.

</details>
