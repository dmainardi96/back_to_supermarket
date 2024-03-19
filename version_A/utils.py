"""
This script contains utility functions used in the checkout system.
"""
from version_A.items_pricing import items_pricing


def print_separator(length):
    """
    Print a separator line with the specified length.

    Args:
        length (int): The length of the separator line.
    """
    separator = '-' * length
    print(separator)


def print_items():
    """Print pricing information for items."""
    print("Running on the following Item pricing:")
    print_separator(40)
    for key, value in items_pricing.items():
        print(value)
    print_separator(40)
