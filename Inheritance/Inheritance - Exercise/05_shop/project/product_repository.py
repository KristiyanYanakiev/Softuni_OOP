from typing import List

from project.product import Product


class ProductRepository:
    products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self) -> str:
        res = ""
        for p in self.products:
            res += f"{p.name}: {p.quantity}\n"

        return res[:-1]

