from models import Item
from version_A.tests import test_prices
from version_A.utils import print_separator

items_pricing = {
    'A': Item('A', 50, special_price=130, special_qty=3),
    'B': Item('B', 30, special_price=45, special_qty=2),
    'C': Item('C', 20),
    'D': Item('D', 15)
}


def print_items():
    print("Esecuzione di test sui seguenti Item pricing:")
    print_separator(40)
    for key, value in items_pricing.items():
        print(value)
    print_separator(40)


if __name__ == '__main__':
    print_items()
    test_prices(items_pricing)
