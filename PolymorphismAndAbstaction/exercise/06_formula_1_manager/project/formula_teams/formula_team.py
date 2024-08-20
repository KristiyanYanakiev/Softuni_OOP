from abc import ABC, abstractmethod
from typing import Dict, List


class FormulaTeam(ABC):
    MIN_BUDGET = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < FormulaTeam.MIN_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        earned_money: int = 0

        for sponsor in self.sponsors.values():  # [{1: 1_500_000, 2: 800_000}, {8: 20_000, 10: 10_000}]
            for pos in sponsor:  # {1: 1_500_000, 2: 800_000} - should be sorted
                if race_pos <= pos:
                    earned_money += sponsor[pos]
                    break

        earned_money -= self.expenses
        self.budget += earned_money
        return f"The revenue after the race is {earned_money}$. Current budget {self.budget}$"

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses(self) -> int:
        pass
