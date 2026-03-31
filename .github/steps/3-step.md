## Step 3: Refactor — Extract a Helper Function

Excellent progress! 🎉 In this step you will use Copilot to refactor duplicated discount logic into a shared helper.

### 📖 Theory: Copilot-Assisted Refactoring

Copilot can suggest refactors when you describe the intent in a comment or a chat prompt. The key technique is:

1. Select the repeated code block.
2. Ask Copilot to extract it into a named helper.
3. Update all call sites to use the new helper.

### ⌨️ Activity: Extract `apply_discount`

1. Open `step-03-refactor/exercise.py`. You will see two functions, `checkout_total` and `invoice_total`, that each apply a percentage discount using identical inline logic.

2. Select the duplicated discount expression in `checkout_total` and prompt Copilot:

   > **Prompt to try:**
   > ```text
   > Refactor the duplicated discount calculation into a helper function called apply_discount(amount, pct) that returns the discounted value. Use it in both checkout_total and invoice_total.
   > ```

3. Verify that the refactored file:
   - Defines `apply_discount(amount, pct)` at module level.
   - Calls `apply_discount` inside `checkout_total` and `invoice_total`.
   - Returns the same results as before.

4. Save and validate:

   ```bash
   python3 scripts/evaluate.py --step step-03
   ```

5. Fill in `step-03-refactor/copilot-evidence.md` with the prompt you used and a brief note on the refactor.

6. Open a pull request targeting `main` with your changes to `step-03-refactor/`.

<details>
<summary>Having trouble? 🤷</summary>

- The test checks that a function named exactly `apply_discount` exists in the module using AST analysis.
- Make sure both `checkout_total` and `invoice_total` still return correct values — run the unit tests locally.
- If Copilot names the helper differently, rename it to `apply_discount`.

</details>
