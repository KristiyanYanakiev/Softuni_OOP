from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):

    INTEREST_RATE = 1.5
    AMOUNT = 2000.0

    def __init__(self):
        super().__init__(self.INTEREST_RATE, self.AMOUNT)

    def increase_interest_rate(self) -> None:
        self.interest_rate += 0.2


