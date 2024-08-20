from abc import ABC, abstractmethod


class BaseWaiter(ABC):

    HOURLY_WAGE = 0
    SHIFT_TYPE = ""
    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 50

    def __init__(self, name: str, hours_worked: int):
        self.name = name
        self.hours_worked = hours_worked
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) < 3 or len(value) > 50:
            raise ValueError(f"Waiter name must be between {self.NAME_MIN_LENGTH} and {self.NAME_MAX_LENGTH} characters in length!")
        self.__name = value

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if value < 0:
            raise ValueError("Cannot have negative hours worked!")
        self.__hours_worked = value

    def calculate_earnings(self) -> float:
        return self.hours_worked * self.HOURLY_WAGE

    def report_shift(self) -> str:
        return f"{self.name} worked a {self.SHIFT_TYPE} shift of {self.hours_worked} hours."

    def __str__(self):
        return f"Name: {self.name}, Total earnings: ${self.calculate_earnings():.2f}"
