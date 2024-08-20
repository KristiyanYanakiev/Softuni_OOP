from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []
        self.equipment_mapper: dict = {
            "KneePad": KneePad,
            "ElbowPad": ElbowPad
        }
        self.team_mapper: dict = {
            "OutdoorTeam": OutdoorTeam,
            "IndoorTeam": IndoorTeam
        }

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.equipment_mapper:
            raise Exception("Invalid equipment type!")
        new_equipment = self.equipment_mapper[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.team_mapper:
            raise Exception("Invalid team type!")

        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."

        new_team = self.team_mapper[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment: BaseEquipment = list(filter(lambda e: e.__class__.__name__ == equipment_type, self.equipment))[-1]
        # found_equipments = [e for e in self.equipment if e.__class__.__name__ == equipment_type]
        # equipment = found_equipments[-1]
        # team: BaseTeam = next(filter(lambda t: t.name == team_name, self.teams))
        found_teams = [team for team in self.teams if team.name == team_name]
        team = found_teams[0]
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            # team: BaseTeam = next(filter(lambda t: t.name == team_name, self.teams))
            team = [t for t in self.teams if t.name == team_name][0]
        except IndexError:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0

        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):

        # first_team: BaseTeam = next(filter(lambda t: t.name == team_name1, self.teams))
        # second_team: BaseTeam = next(filter(lambda t: t.name == team_name2, self.teams))

        first_team = [t for t in self.teams if t.name == team_name1][0]
        second_team = [t for t in self.teams if t.name == team_name2][0]

        if not first_team.__class__.__name__ == second_team.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        fist_team_score = sum(e.protection for e in first_team.equipment) + first_team.advantage
        second_team_score = sum(e.protection for e in second_team.equipment) + second_team.advantage

        if fist_team_score == second_team_score:
            return "No winner in this game."

        winner_team: BaseTeam = first_team if fist_team_score > second_team_score else second_team
        winner_team.win()
        return f"The winner is {winner_team.name}."

    def get_statistics(self):

        sorted_teams = sorted(self.teams, key=lambda t: - t.wins)
        result = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n"

        result += "\n".join(t.get_statistics() for t in sorted_teams)
        return result[:-1]

        # for team in sorted_teams:
        #     result += f"{team.get_statistics()}\n"
        #
        # return result[:-1]
