# Copilot Evidence — Step 03

## Refactor prompt

Asked Copilot to refactor the duplicated discount logic in `checkout_total` and `invoice_total` into a shared helper function called `apply_discount`.

## Why behavior is preserved

The `apply_discount` helper contains the exact same discount calculation logic that was previously duplicated: check if discount is non-positive, compute discount amount, subtract from subtotal, clamp to zero, and round. Both functions now delegate to this helper.

## Before vs after summary

Before: Both functions had identical 6-line discount blocks. After: Shared `apply_discount(subtotal, discount_percent)` helper eliminates duplication while keeping the same input/output behavior.
