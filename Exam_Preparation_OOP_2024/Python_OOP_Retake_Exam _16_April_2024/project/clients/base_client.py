from abc import ABC, abstractmethod
from typing import Tuple


class BaseClient(ABC):

    VALID_MEMBERSHIPS = ["Regular", "VIP"]

    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in self.VALID_MEMBERSHIPS:
            raise ValueError(f"Invalid membership type. Allowed types: {', '.join(self.VALID_MEMBERSHIPS)}.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float) -> int:
        pass

    def apply_discount(self) -> Tuple[int, int]:

        if self.points >= 100:
            discount = 10
            used_points = 100
            self.points -= used_points
            return discount, self.points

        if 50 <= self.points < 100:
            discount = 5
            used_points = 50
            self.points -= used_points
            return discount, self.points

        if self.points < 50:
            discount = 0
            used_points = 0
            self.points -= used_points
            return discount, self.points











