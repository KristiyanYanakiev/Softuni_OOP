from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):

    INITIAL_BUDGET = 500.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.INITIAL_BUDGET)

    def win(self) -> None:
        self.advantage += 145
        self.wins += 1
