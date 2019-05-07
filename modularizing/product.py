import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_UP


class Product(object):
    def __init__(self, name: str, price, category: str, sku=str()):
        self.name = name
        self.category = category
        self.price = Decimal(price)
        self.sku = sku

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price = self.price * Decimal((1 + percent_change / 100))
        else:
            self.price = self.price * Decimal((1 - percent_change / 100))

    def print_info(self):
        print("{:<20}{:<20}{:>10}".format(self.name[:18], self.category, round(self.price, 2)))
