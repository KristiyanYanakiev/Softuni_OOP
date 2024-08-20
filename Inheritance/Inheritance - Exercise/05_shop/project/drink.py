from project.product import Product


class Drink(Product):

    quantity = 10

    def __init__(self, name: str) -> None:
        super().__init__(name, self.quantity)


