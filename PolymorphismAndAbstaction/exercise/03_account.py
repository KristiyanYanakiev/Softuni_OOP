from typing import List


class Account:

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: List[int] = []

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def handle_transaction(self, transaction_amount: int or str) -> str or ValueError:
        if self.balance + transaction_amount <= 0:
            self.insufficient_balance()

        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int) -> str or ValueError:
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        if self.balance + amount <= 0:
            self.insufficient_balance()

        self._transactions.append(amount)
        return f"New balance: {self.balance}"


    @staticmethod
    def insufficient_balance() -> ValueError:
        raise ValueError("sorry cannot go in debt!")

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, idx: int):
        return self._transactions[idx]

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __add__(self, other):
        new_instance = type(self)(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_instance._transactions = self._transactions + other._transactions

        return new_instance