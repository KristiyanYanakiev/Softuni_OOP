from typing import List

from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:

    valid_names: List[str] = ["Red Bull", "Mercedes"]

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int) -> str or ValueError:
        if team_name in self.valid_names:
            if team_name == self.valid_names[0]:
                self.red_bull_team = RedBullTeam(budget)
            else:
                self.mercedes_team = MercedesTeam(budget)
            return f"{team_name} has joined the new F1 season."

        raise ValueError("Invalid team name!")

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int) -> str or Exception:

        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        team_with_better_pos = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        return (f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. "
                f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. "
                f"{team_with_better_pos} is ahead at the {race_name} race.")
