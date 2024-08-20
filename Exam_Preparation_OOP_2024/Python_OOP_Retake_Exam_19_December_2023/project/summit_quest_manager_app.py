from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBER_TYPES = ["ArcticClimber", "SummitClimber"]
    VALID_PEAK_TYPES = ["ArcticPeak", "SummitPeak"]

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str) -> str or None:
        if climber_type not in self.VALID_CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        try:
            searched_climber = next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."
        except StopIteration:
            if climber_type == "ArcticClimber":
                c = ArcticClimber(climber_name)
            else:
                c = SummitClimber(climber_name)

            self.climbers.append(c)
            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."

        if peak_type == "ArcticPeak":
            p = ArcticPeak(peak_name, peak_elevation)
        else:
            p = SummitPeak(peak_name, peak_elevation)

        self.peaks.append(p)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):

        c: BaseClimber = next(filter(lambda c: c.name == climber_name, self.climbers))
        if gear == c.climber_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        missing_gear = [el for el in c.climber_gear if el not in gear]
        c.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):

        try:
            searched_climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak: BasePeak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if searched_climber.can_climb() and searched_climber.is_prepared:
            searched_climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        if not searched_climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        searched_climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):

        total_climbed_peaks: List[BasePeak] = []
        final_climbers_list: List[BaseClimber] = []

        for c in self.climbers:
            if c.conquered_peaks:
                final_climbers_list.append(c)
                if len(c.conquered_peaks) > 1:
                    c.conquered_peaks = sorted(c.conquered_peaks)
            total_climbed_peaks.extend(c.conquered_peaks)

        sorted_final_climbers_list = sorted(final_climbers_list,
                                            key=lambda c: (-len(c.conquered_peaks), c.name))

        result = f"Total climbed peaks: {len(set(total_climbed_peaks))}\n**Climber's statistics:**"
        climber_stats = "\n".join(str(c) for c in sorted_final_climbers_list)
        result += f"\n{climber_stats}"

        return result

#  TODO: Find possible sources of Runtime error


