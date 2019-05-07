from .product import Product
from .store import Store


def test_store():
    store = Store("Toy store")
    store.add_product(Product("barbie", 7.77, "doll"))
    store.add_product(Product("g i joe", 4.77, "doll"))
    store.add_product(Product("Zelda II: The adventure of Link", 50.3, "video game", sku="abcdef"))

    store.inventory()
    store.set_clearance('doll', 50)
    store.inventory()

    store.sell_product(sku="abcdef")
    store.sell_product(id=0)
    store.inventory()
