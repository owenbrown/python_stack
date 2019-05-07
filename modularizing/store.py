from typing import List

from .product import Product


class Store(object):
    def __init__(self, name, products: List[Product] = None):
        self.name = name
        self.products = products or []  # type: List[Product]

    def add_product(self, new_product: Product):
        self.products.append(new_product)

    def sell_product(self, id: str=None, sku: str=None):
        if sku:
            try:
                id = [p.sku for p in self.products].index(sku)

            except ValueError:
                print("sku wasn't found!")
                return

        product = self.products.pop(int(id))
        product.print_info()

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for product in filter(lambda p: p.category == category, self.products):
            product.update_price(percent_discount, False)


    def inventory(self):
        print("The store's inventory")
        for product in self.products:
            product.print_info()
