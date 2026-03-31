# Step 03 — Refactoring

## Copilot Feature
Chat-guided refactoring

## Criteria
1. A helper function named `apply_discount` exists and encapsulates shared discount logic.
2. `checkout_total` and `invoice_total` both delegate to `apply_discount` (no duplicated discount calculation).
3. All public function signatures remain unchanged.
4. Behavior is preserved: totals unchanged for valid inputs, edge cases work (empty list, discount 0, discount 100).
5. `copilot-evidence.md` contains the word "refactor" and shows genuine Copilot-assisted refactoring process.
