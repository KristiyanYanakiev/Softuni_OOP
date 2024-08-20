from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @property
    @abstractmethod
    def increase_of_fuel_consumption_due_to_air_conditioner(self):
        pass

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    @property
    def increase_of_fuel_consumption_due_to_air_conditioner(self):
        return 0.9

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.increase_of_fuel_consumption_due_to_air_conditioner)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    KEPT_FUEL: float = 0.95

    @property
    def increase_of_fuel_consumption_due_to_air_conditioner(self):
        return 1.6

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.increase_of_fuel_consumption_due_to_air_conditioner)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.KEPT_FUEL



truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)