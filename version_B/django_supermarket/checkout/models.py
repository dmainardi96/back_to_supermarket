from django.db import models


# Model representing an item in the store
class Item(models.Model):
    sku = models.CharField(max_length=50, unique=True)  # Unique SKU code to identify the item
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Model representing the price of an item over time
class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    start_date = models.DateField()  # Start date of the price validity
    end_date = models.DateField(null=True, blank=True)  # End date of the price validity (optional)
    price = models.FloatField()

    def __str__(self):
        return f"{self.item.name} - {self.price}"


# Model representing a discount applicable to an item or combination of items
class Discount(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()  # Start date of the discount validity
    end_date = models.DateField(null=True, blank=True)  # End date of the discount validity (optional)
    discount_quantity = models.PositiveIntegerField(default=0)  # Quantity of items to trigger the discount
    discount_value = models.FloatField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
