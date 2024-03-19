def price(pricing_rules, user_cart):
    totals_cart = dict()
    for element in user_cart:
        totals_cart = scan(element, totals_cart)

    total_price = calculate_total(totals_cart, pricing_rules)

    return total_price


def scan(sku, totals_cart):
    """Adds an item to the cart by its SKU."""
    # TODO
    return


def calculate_total(totals_cart, pricing_rules):
    """Calculates and returns the total price for all items in the cart."""
    # TODO
    return
