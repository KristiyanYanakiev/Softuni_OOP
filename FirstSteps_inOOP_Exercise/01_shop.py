from typing import List


class Shop:
    def __init__(self, name: str, items: List[str]):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])

shop2 = Shop("Second shop", ["cars", "stuf"])
print(shop.get_items_count())
print(shop2.get_items_count())