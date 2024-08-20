from abc import ABC, abstractmethod
from typing import List

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):

    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: List[BaseBattleship] = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value: str):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self) -> List[BaseBattleship]:

        sorted_ships = sorted(self.ships, key=lambda sh: - sh.hit_strength)

        final_sorted_ships = sorted(sorted_ships, key=lambda sh: sh.name)

        return final_sorted_ships

    @abstractmethod
    def zone_info(self):
        pass
