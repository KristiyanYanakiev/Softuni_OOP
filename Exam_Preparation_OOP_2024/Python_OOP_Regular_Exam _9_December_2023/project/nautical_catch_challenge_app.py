from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = ["FreeDiver", "ScubaDiver"]
    VALID_FISH_TYPES = ["PredatoryFish", "DeepSeaFish"]

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):

        if diver_type not in self.VALID_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
            return f"{diver_name} is already a participant."
        except StopIteration:
            if diver_type == self.VALID_DIVER_TYPES[0]:
                created_driver = FreeDiver(diver_name)
            else:
                created_driver = ScubaDiver(diver_name)
            self.divers.append(created_driver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."
        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
            return f"{fish_name} is already permitted."
        except StopIteration:
            if fish_type == self.VALID_FISH_TYPES[0]:
                created_fish = PredatoryFish(fish_name, points)
            else:
                created_fish = DeepSeaFish(fish_name, points)
            self.fish_list.append(created_fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver: BaseDiver = next(filter(lambda d: d.name == diver_name, self.divers))
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            fish: BaseFish = next(filter(lambda f: f.name == fish_name, self.fish_list))
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        message = ""

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                message = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.update_health_status()

        return message

    def health_recovery(self):
        divers_recovered = 0

        for diver in self.divers:

            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy()
                divers_recovered += 1

        return f"Divers recovered: {divers_recovered}"

    def diver_catch_report(self, diver_name: str):
        searched_diver: BaseDiver = next(filter(lambda d: d.name == diver_name, self.divers))
        res = f"**{diver_name} Catch Report**\n"
        res += "\n".join(fish.fish_details() for fish in searched_diver.catch)

        return res

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(healthy_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        res = f"**Nautical Catch Challenge Statistics**\n"
        res += f"\n".join(str(d) for d in sorted_divers)

        return res
