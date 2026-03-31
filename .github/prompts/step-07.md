# Step 07 — Debugging Assistance

## Copilot Feature
Debugging via chat assistance and `/fix`

## Criteria
1. Bugs in `summarize_response_times` are identified and fixed:
   - Correctly computes min, max, and average
   - Ignores negative values
   - Handles empty or all-invalid input safely
2. Output schema is preserved (returns the expected dict structure).
3. Fix does not introduce new logic bugs.
4. `copilot-evidence.md` contains the words "debug" and "/fix" and documents the debugging thought process.
