from datetime import date
from django.test import TestCase
from checkout.checkout_system import CheckoutSystem
from checkout.models import Item, Price, Discount


class CheckoutPricingTestCase(TestCase):
    def setUp(self):
        """
        Prepare test data in the database.
        """
        today = date.today()

        # Create test items
        self.item_A = Item.objects.create(sku='A', name='Item A')
        self.item_B = Item.objects.create(sku='B', name='Item B')
        self.item_C = Item.objects.create(sku='C', name='Item C')
        self.item_D = Item.objects.create(sku='D', name='Item D')

        # Create prices with start_date as today and end_date as None
        Price.objects.create(item=self.item_A, price=50, start_date=today, end_date=None)
        Price.objects.create(item=self.item_B, price=30, start_date=today, end_date=None)
        Price.objects.create(item=self.item_C, price=20, start_date=today, end_date=None)
        Price.objects.create(item=self.item_D, price=15, start_date=today, end_date=None)

        # Create discounts
        Discount.objects.create(item=self.item_A, discount_value=130, discount_quantity=3,
                                start_date=today, end_date=None)
        Discount.objects.create(item=self.item_B, discount_value=45, discount_quantity=2,
                                start_date=today, end_date=None)

    def test_empty_cart(self):
        """
        Test an empty cart.
        """
        checkout_system = CheckoutSystem()
        checkout_system.set_cart("")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 0)

    def test_single_item(self):
        """
        Test prices for individual items.
        """
        checkout_system = CheckoutSystem()

        # Test "A"
        checkout_system.set_cart("A")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 50)

        # Test "B"
        checkout_system.set_cart("B")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 30)

        # Test "C"
        checkout_system.set_cart("C")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 20)

        # Test "D"
        checkout_system.set_cart("D")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 15)

    def test_multiple_items(self):
        """
        Test prices for multiple items.
        """
        checkout_system = CheckoutSystem()

        # Test "AB"
        checkout_system.set_cart("AB")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 80)

        # Test "CDBA"
        checkout_system.set_cart("CDBA")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 115)

        # Test "AA"
        checkout_system.set_cart("AA")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 100)

        # Test "AAA"
        checkout_system.set_cart("AAA")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 130)

        # Test "AAAA"
        checkout_system.set_cart("AAAA")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 180)

        # Test "AAAAA"
        checkout_system.set_cart("AAAAA")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 230)

        # Test "AAAAAA"
        checkout_system.set_cart("AAAAAA")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 260)

        # Test "AAAB"
        checkout_system.set_cart("AAAB")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 160)

        # Test "AAABB"
        checkout_system.set_cart("AAABB")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 175)

        # Test "AAABBD"
        checkout_system.set_cart("AAABBD")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 190)

        # Test "DABABA"
        checkout_system.set_cart("DABABA")
        total_price = checkout_system.price()
        self.assertEqual(total_price, 190)
