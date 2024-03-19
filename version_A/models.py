class Item:
    def __init__(self, sku, unit_price, special_qty=None, special_price=None):
        self.sku = sku
        self.unit_price = unit_price
        self.special_qty = special_qty
        self.special_price = special_price

    def __str__(self):
        if self.special_price:
            return "Item {}. Unit price: {}, Special Price: {} for {} units".format(
                self.sku, self.unit_price, self.special_price, self.special_qty)
        else:
            return "Item {}. Unit price: {}. No discounts.".format(
                self.sku, self.unit_price)