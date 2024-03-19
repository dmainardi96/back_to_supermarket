"""
This script defines the data models used in the checkout system.
"""

from typing import Optional


class Item:
    """Represents an item in the checkout system with pricing information."""

    def __init__(self, sku: str, unit_price: int,
                 special_qty: Optional[int] = None,
                 special_price: Optional[int] = None) -> None:
        """
        Initializes a new Item object.

        Args:
            sku (str): SKU code of the item.
            unit_price (float): Unit price of the item.
            special_qty (int, optional): Quantity to obtain the special offer (default is None).
            special_price (float, optional): Special price if there's a discount activated (default is None).
        """

        self.sku = sku
        self.unit_price = unit_price
        self.special_qty = special_qty
        self.special_price = special_price

    def __str__(self) -> str:
        if self.special_price:
            return f"Item {self.sku}. Unit price: {self.unit_price}, " \
                   f"Special Price: {self.special_price} for {self.special_qty} units"
        else:
            return f"Item {self.sku}. Unit price: {self.unit_price}. No discounts."
