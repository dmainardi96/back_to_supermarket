"""
Module containing pricing information for items.

To update pricing:
1. Edit values in items_pricing dictionary.
2. Each key-value pair represents an item and its pricing.
3. Update values for SKU, unit price, special price (if any), and special quantity (if any).
"""

from version_A.models import Item

# Dictionary containing pricing information for items
items_pricing = {
    'A': Item('A', 50, special_price=130, special_qty=3),  # Modify these lines
    'B': Item('B', 30, special_price=45, special_qty=2),
    'C': Item('C', 20),
    'D': Item('D', 15)
}
