from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    VALID_TYPES = ["Laptop", "Desktop Computer"]

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price: int = 0

    @staticmethod
    def is_power_of_two(n):
        result = log2(n)
        return result.is_integer()

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    @abstractmethod
    def type(self):
        pass

    def configure_computer(self, processor: str, ram: int) -> str:
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        if ram > self.max_ram or not self.is_power_of_two(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += self.available_processors[processor]
        self.price += int(log2(ram)) * 100

        return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
