from math import floor

from project.clients.base_client import BaseClient


class RegularClient(BaseClient):

    MEMBERSHIP_TYPE = "Regular"

    def __init__(self, name):
        super().__init__(name, self.MEMBERSHIP_TYPE)

    def earning_points(self, order_amount: float) -> int:
        earned_points = floor(order_amount / 10)
        self.points += earned_points
        return earned_points



