"""
This script contains utility functions.
"""
from items_pricing import items_pricing
import functools

def print_separator(length):
    """
    Print a separator line with the specified length.

    Args:
        length (int): The length of the separator line.
    """
    separator = '-' * length
    print(separator)


def print_items():
    print("Running on the following Item pricing:")
    print_separator(40)
    for key, value in items_pricing.items():
        print(value)
    print_separator(40)


def print_items_decorator(func):
    """Decorator for handling items_pricing on annotated functions."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print_items()
        response = func(*args, **kwargs)
        return response

    return wrapper
