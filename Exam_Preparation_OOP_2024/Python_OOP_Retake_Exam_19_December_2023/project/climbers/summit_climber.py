from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    MINIMUM_STRENGTH = 75

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)
        self.climber_gear = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def can_climb(self):
        if self.strength >= self.MINIMUM_STRENGTH:
            return True
        return False

    def climb(self, peak: BasePeak) -> None:
        if peak.difficulty_level == "Advanced":
            self.strength -= 30 * 1.3

        else:
            self.strength -= 30 * 2.5

        self.conquered_peaks.append(peak.name)
