def price(pricing_rules, user_cart):
    totals_cart = dict()
    for element in user_cart:
        totals_cart = scan(element, totals_cart)

    total_price = calculate_total(totals_cart, pricing_rules)

    return total_price


def scan(sku, totals_cart):
    """Adds an item to the cart by its SKU."""
    if sku in totals_cart:
        totals_cart[sku] += 1
    else:
        totals_cart[sku] = 1

    return totals_cart


def calculate_total(totals_cart, pricing_rules):
    """Calculates and returns the total price for all items in the cart."""
    total_price = 0
    for sku, qty in totals_cart.items():
        if sku in pricing_rules:
            item = pricing_rules[sku]
            if item.special_qty and qty >= item.special_qty:
                special_count = qty // item.special_qty
                remaining_qty = qty % item.special_qty
                total_price += special_count * item.special_price + remaining_qty * item.unit_price
            else:
                total_price += qty * item.unit_price

    return total_price