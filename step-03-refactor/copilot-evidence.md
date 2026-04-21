# Copilot Evidence — Step 03

Refactoring exercise to eliminate duplication using GitHub Copilot.

## Refactor prompt

"Refactor this file to remove duplicated discount logic by extracting a helper function named `apply_discount` that both `checkout_total` and `invoice_total` can use. Keep all public function signatures unchanged."

## Refactoring approach

Copilot identified the duplicated logic:
1. Both functions had identical discount calculation logic
2. The pattern: calculate subtotal, apply discount percentage, ensure non-negative result, round to 2 decimals
3. Extracted this into a reusable `apply_discount(subtotal, discount_percent)` helper function
4. Modified `checkout_total` and `invoice_total` to use the helper while maintaining their original signatures

## Why behavior is preserved

- The `apply_discount` helper contains the exact same logic that was duplicated
- Both `checkout_total` and `invoice_total` now call this helper with the same parameters
- The function signatures for the public functions remain unchanged
- All edge cases are handled identically: empty lists, 0% discount, 100% discount, negative results

## Before vs after summary

**Before**: 40 lines of code with duplicated discount logic in two functions

**After**: 34 lines with a shared `apply_discount` helper that:
- Reduces code duplication
- Makes the discount logic easier to maintain
- Improves readability by making intent clearer
- Preserves all existing behavior and edge case handling

## Code quality improvements

- DRY principle (Don't Repeat Yourself) applied
- Helper function has clear responsibility and documentation
- Easier to update discount logic in the future (single location)
- Behavior is identical to the original implementation
