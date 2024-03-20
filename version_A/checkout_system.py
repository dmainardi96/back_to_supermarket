from typing import Dict

from models import Item

"""
This module implements business logic functions for the checkout system.

Functions:
    price: Create total items in cart, calculate the total price of the user's cart.
    scan: Add an item to the cart by its SKU.
    calculate_total: Calculate the total price for all items in the cart.
"""


def price(pricing_rules: Dict[str, Item], user_cart: str) -> int:
    """
    Create total items in cart, then calculate the total price of the user's cart.

    Args:
        pricing_rules (Dict[str, Item]): Dictionary containing pricing rules for items.
        user_cart (str): String representing the user's cart.

    Returns:
        int: The total price of the user's cart.
    """
    totals_cart = dict()
    for element in user_cart:
        totals_cart = scan(element, totals_cart)

    total_price = calculate_total(totals_cart, pricing_rules)
    print(f"Total price for your cart: {total_price}")

    return total_price


def scan(sku: str, totals_cart: Dict[str, int]) -> Dict[str, int]:
    """
    Add an item to the cart by its SKU.

    Args:
        sku (str): SKU of the item to add to the cart.
        totals_cart (Dict[str, int]): Dictionary containing the total count of items in the cart.

    Returns:
        Dict[str, int]: Updated dictionary containing the total count of items in the cart.
    """
    if sku in totals_cart:
        totals_cart[sku] += 1
    else:
        totals_cart[sku] = 1

    return totals_cart


def calculate_total(totals_cart: Dict[str, int], pricing_rules: Dict[str, Item]) -> int:
    """
    Calculate and return the total price for all items in the cart.

    Args:
        totals_cart (Dict[str, int]): Dictionary containing the total count of items in the cart.
        pricing_rules (Dict[str, Item]): Dictionary containing pricing rules for items.

    Returns:
        int: The total price for all items in the cart.
    """
    total_price = 0
    not_valid_skus = list()
    for sku, quantity in totals_cart.items():
        if sku in pricing_rules:
            item = pricing_rules[sku]
            if item.special_qty and quantity >= item.special_qty:
                # Calculate the number of times the special offer applies and the remaining quantity
                # Eg. 4 A -> Discount of 3 A + Single A price
                special_count, remaining_qty = divmod(quantity, item.special_qty)
                total_price += special_count * item.special_price + remaining_qty * item.unit_price
            else:
                total_price += quantity * item.unit_price
        else:
            not_valid_skus.append(sku)

    if not_valid_skus:
        print(f"Not valid skus: {not_valid_skus}")

    return total_price
