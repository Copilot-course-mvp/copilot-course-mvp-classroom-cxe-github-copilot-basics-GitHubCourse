def apply_discount(subtotal: float, discount_percent: float) -> float:
    if discount_percent <= 0:
        return round(subtotal, 2)
    discount = subtotal * (discount_percent / 100)
    total = subtotal - discount
    if total < 0:
        total = 0
    return round(total, 2)


def checkout_total(items: list[float], discount_percent: float) -> float:
    subtotal = 0.0
    for value in items:
        subtotal += value
    return apply_discount(subtotal, discount_percent)


def invoice_total(lines: list[float], discount_percent: float) -> float:
    subtotal = 0.0
    for value in lines:
        subtotal += value
    return apply_discount(subtotal, discount_percent)