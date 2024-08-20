from typing import List

from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.clients.base_client import BaseClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_WAITER_TYPES = ["FullTimeWaiter", "HalfTimeWaiter"]
    VALID_CLIENT_TYPES = ["RegularClient", "VIPClient"]

    def __init__(self):
        self.waiters = []
        self.clients = []


    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.VALID_WAITER_TYPES:
            return f"{waiter_type} is not a recognized waiter type."
        try:
            waiter = next(filter(lambda w: w.name == waiter_name, self.waiters))
            return f"{waiter_name} is already on the staff."
        except StopIteration:
            if waiter_type == "FullTimeWaiter":
                waiter = FullTimeWaiter(waiter_name, hours_worked)
                self.waiters.append(waiter)
                return f"{waiter_name} is successfully hired as a {waiter_type}."

            waiter = HalfTimeWaiter(waiter_name, hours_worked)
            self.waiters.append(waiter)
            return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.VALID_CLIENT_TYPES:
            return f"{client_type} is not a recognized client type."
        try:
            client = next(filter(lambda c: c.name == client_name, self.clients))
            return f"{client_name} is already a client."
        except StopIteration:
            if client_type == "RegularClient":
                client = RegularClient(client_name)
                self.clients.append(client)
                return f"{client_name} is successfully admitted as a {client_type}."

            client = VIPClient(client_name)
            self.clients.append(client)
            return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str) -> str:
        try:
            waiter: BaseWaiter = next(filter(lambda w: w.name == waiter_name, self.waiters))
            return waiter.report_shift()
        except StopIteration:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float) -> str:
        try:
            client: BaseClient = next(filter(lambda c: c.name == client_name, self.clients))
            return f"{client_name} earned {client.earning_points(order_amount)} points from the order."
        except StopIteration:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str) -> str:
        try:
            client: BaseClient = next(filter(lambda c: c.name == client_name, self.clients))
            return (f"{client_name} received a {client.apply_discount()[0]}% discount. "
                    f"Remaining points {client.points}")
        except StopIteration:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self) -> str:
        total_earnings = sum([w.calculate_earnings() for w in self.waiters])
        total_clients_unused_points = sum([c.points for c in self.clients])
        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)
        joined_waiters = "\n".join(str(w) for w in sorted_waiters)

        return (f"$$ Monthly Report $$\n"
                f"Total Earnings: ${total_earnings:.2f}\n"
                f"Total Clients Unused Points: {total_clients_unused_points}\n"
                f"Total Clients Count: {len(self.clients)}\n"
                f"** Waiter Details **\n{joined_waiters}")
