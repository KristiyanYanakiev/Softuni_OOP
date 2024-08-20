from abc import ABC

from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def allowed_foods(self):
        return [Vegetable, Fruit]

    @property
    def weight_increase_per_quantity_of_food(self) -> float:
        return 0.10


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def allowed_foods(self):
        return [Meat]

    @property
    def weight_increase_per_quantity_of_food(self) -> float:
        return 0.40


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def allowed_foods(self):
        return [Vegetable, Meat]

    @property
    def weight_increase_per_quantity_of_food(self) -> float:
        return 0.30


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def allowed_foods(self):
        return [Meat]

    @property
    def weight_increase_per_quantity_of_food(self) -> float:
        return 1.00
