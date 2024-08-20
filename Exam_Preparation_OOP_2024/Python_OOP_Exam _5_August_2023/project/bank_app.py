from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    valid_loans_mapper = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    valid_clients_mapper = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []
        self.granted_loans: List[BaseLoan] = []

    def add_loan(self, loan_type: str) -> str or Exception:
        if loan_type not in self.valid_loans_mapper:
            raise Exception("Invalid loan type!")
        created_loan = self.valid_loans_mapper[loan_type]()
        self.loans.append(created_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str or Exception:
        if client_type not in self.valid_clients_mapper:
            raise Exception("Invalid client type!")

        if self.capacity == len(self.clients):
            return "Not enough bank capacity."

        created_client = self.valid_clients_mapper[client_type](client_name, client_id, income)
        self.clients.append(created_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):

        client = [c for c in self.clients if c.client_id == client_id][0]
        if client.__class__.__name__ == "Student" and loan_type == "StudentLoan":
            loan = [l for l in self.loans if l.__class__.__name__ == "StudentLoan"][0]
            self.loans.remove(loan)
            client.loans.append(loan)
            self.granted_loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        if client.__class__.__name__ == "Adult" and loan_type == "MortgageLoan":
            loan = [l for l in self.loans if l.__class__.__name__ == "MortgageLoan"][0]
            self.loans.remove(loan)
            client.loans.append(loan)
            self.granted_loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        try:
            client_to_remove = [c for c in self.clients if c.client_id == client_id][0]
        except IndexError:
            raise Exception("No such client!")

        if client_to_remove.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client_to_remove)
        return f"Successfully removed {client_to_remove.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0

        for l in self.loans:
            if l.__class__.__name__ == loan_type:
                l.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0

        for c in self.clients:
            if c.interest < min_rate:
                c.increase_clients_interest()
                changed_client_rates_number += 1
        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):

        result = [f"Active Clients: {len(self.clients)}", f"Total Income: {sum(c.income for c in self.clients):.2f}",
                  f"Granted Loans: {len(self.granted_loans)}, Total Sum: {sum(l.amount for l in self.granted_loans):.2f}",
                  f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}",
                  f"Average Client Interest Rate: "
                  f"{sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0:.2f}"]

        return "\n".join(result)


