from datetime import date
from typing import Dict
from django.db.models import Q
from checkout.models import Price, Discount


class CheckoutSystem:
    def __init__(self, cart: str = None):
        self.cart = cart
        self.pricing_rules = self.get_prices_and_discounts()

    def set_cart(self, cart: str) -> None:
        self.cart = cart

    def get_prices_and_discounts(self) -> Dict:
        """
        Retrieve pricing rules (prices and discounts) from the database.
        """
        today = date.today()

        prices = Price.objects.filter(
            Q(start_date__lte=today) & (Q(end_date__gte=today) | Q(end_date__isnull=True))
        ).values_list('item__sku', 'price')

        discounts = Discount.objects.filter(
            Q(start_date__lte=today) & (Q(end_date__gte=today) | Q(end_date__isnull=True))
        ).values_list('item__sku', 'discount_value', 'discount_quantity')

        # Create dictionaries for prices and discounts
        prices_dict = {sku: {'price': price} for sku, price in prices}
        discounts_dict = {sku: {'discount_value': discount_value,
                                'discount_quantity': discount_quantity} for sku, discount_value, discount_quantity in
                          discounts}

        # Merge dictionaries
        return {sku: {'price': prices_dict.get(sku, {}).get('price'),
                      'discount_value': discounts_dict.get(sku, {}).get('discount_value'),
                      'discount_quantity': discounts_dict.get(sku, {}).get('discount_quantity')}
                for sku in set(prices_dict) | set(discounts_dict)}

    def price(self) -> int:
        """
        Calculate the total price of the user's cart.
        """
        totals_cart = self._create_totals_cart()

        print(f"Total elements in cart: {totals_cart}")
        total_price = self.calculate_total(totals_cart)
        print(f"Total price for your cart: {total_price}")

        return total_price

    def scan(self, sku: str, totals_cart: Dict[str, int]) -> Dict[str, int]:
        """
        Add an item to the cart by its SKU.
        """
        if sku in totals_cart:
            totals_cart[sku] += 1
        else:
            totals_cart[sku] = 1

        return totals_cart

    def calculate_total(self, totals_cart) -> int:
        """
        Calculate the total price for all items in the cart.
        """

        total_price = 0
        not_valid_skus = list()

        for sku, quantity in totals_cart.items():
            if sku in self.pricing_rules:
                item = self.pricing_rules[sku]
                if item["discount_quantity"] and quantity >= item["discount_quantity"]:
                    # Apply discount if applicable
                    # Calculate the number of times the special offer applies and the remaining quantity
                    # Eg. 4 A -> Discount of 3 A + Single A price
                    special_count, remaining_qty = divmod(quantity, item["discount_quantity"])
                    total_price += (special_count * item["discount_value"]) + (remaining_qty * item["price"])
                else:
                    total_price += quantity * item["price"]
            else:
                not_valid_skus.append(sku)

        if not_valid_skus:
            print(f"Not valid skus: {not_valid_skus}")

        return total_price

    def _create_totals_cart(self) -> Dict[str, int]:
        """
        Create total items in cart.
        """
        totals_cart = dict()
        for element in self.cart:
            totals_cart = self.scan(element, totals_cart)
        return totals_cart
