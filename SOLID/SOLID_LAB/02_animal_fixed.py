from abc import ABC, abstractmethod


class Animal(ABC):

    def get_species(self):
        return self.__class__.__name__

    @abstractmethod
    def species_sound(self) -> str:
        pass


class Cat(Animal):

    def species_sound(self) -> str:
        return "meow"


class Dog(Animal):

    def species_sound(self) -> str:
        return "woof-woof"


class Chicken(Animal):

    def species_sound(self) -> str:
        return "quack-quack"


def animal_sound(some_animals: list[Animal]):
    for animal in some_animals:
        print(animal.get_species())
        print(animal.species_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)


