"""
Main script to run tests on item pricing and print the pricing information for items.
"""

from version_A.checkout_system import price
from version_A.items_pricing import items_pricing
from version_A.utils import print_items


def get_user_cart() -> str:
    """
    Prompt the user to enter their cart items.

    Returns:
        str: String representing the user's cart.
    """
    user_cart = input("Enter your cart items (e.g., 'ABCD'): ")
    return user_cart


def main():
    """
    Main function to handle checkout operations.
    """
    print_items()
    user_cart = get_user_cart()  # Prompt user to enter cart items
    price(items_pricing, user_cart)  # Calculate total price


if __name__ == "__main__":
    main()
