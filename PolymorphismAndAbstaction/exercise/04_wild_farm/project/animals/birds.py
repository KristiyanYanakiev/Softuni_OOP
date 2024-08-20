from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):

    @property
    def allowed_foods(self):
        return [Meat]

    @property
    def weight_increase_per_quantity_of_food(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def allowed_foods(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def weight_increase_per_quantity_of_food(self):
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"



