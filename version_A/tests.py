"""
This script contains test cases for the pricing function in the checkout system.
"""

from typing import Dict
from version_A.checkout_system import price
from version_A.items_pricing import items_pricing
from version_A.models import Item
from version_A.utils import print_items


def test_prices(items_pricing: Dict[str, Item]) -> None:
    """
    Run acceptance tests for the pricing function.

    Args:
        items_pricing (Dict[str, Item]): Dictionary containing pricing information for items.
    """

    # Acceptance tests
    assert price(items_pricing, "") == 0
    print("Test with 0 items passed\n")

    assert price(items_pricing, "A") == 50
    print("Test A passed\n")

    assert price(items_pricing, "AB") == 80
    print("Test AB passed\n")

    assert price(items_pricing, "CDBA") == 115
    print("Test CDBA passed\n")

    assert price(items_pricing, "AA") == 100
    print("Test AA passed\n")

    assert price(items_pricing, "AAA") == 130
    print("Test AAA passed\n")

    assert price(items_pricing, "AAAA") == 180
    print("Test AAAA passed\n")

    assert price(items_pricing, "AAAAA") == 230
    print("Test AAAAA passed\n")

    assert price(items_pricing, "AAAAAA") == 260
    print("Test AAAAAA passed\n")

    assert price(items_pricing, "AAAB") == 160
    print("Test AAAB passed\n")

    assert price(items_pricing, "AAABB") == 175
    print("Test AAABB passed\n")

    assert price(items_pricing, "AAABBD") == 190
    print("Test AAABBD passed\n")

    assert price(items_pricing, "DABABA") == 190
    print("Test DABABA passed\n")


if __name__ == '__main__':
    print_items()  # Print pricing information
    test_prices(items_pricing)  # Run tests on item pricing
