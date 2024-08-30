from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    valid_computer_types_mapper = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):

        if type_computer not in self.valid_computer_types_mapper:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        created_computer: Computer = self.valid_computer_types_mapper[type_computer](manufacturer, model)

        configuration: str = created_computer.configure_computer(processor, ram)

        self.warehouse.append(created_computer)

        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):

        try:
            computer = [c for c in self.warehouse if c.price <= client_budget
                        and c.processor == wanted_processor
                        and c.ram >= wanted_ram][0]

        except IndexError:
            raise Exception("Sorry, we don't have a computer for you.")

        profit = client_budget - computer.price
        self.profits += profit
        self.warehouse.remove(computer)

        return f"{computer} sold for {client_budget}$."
