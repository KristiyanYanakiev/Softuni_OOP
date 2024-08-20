from project.climbers.base_climber import BaseClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    MINIMUM_STRENGTH = 100

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)
        self.climber_gear = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def can_climb(self):
        if self.strength >= self.MINIMUM_STRENGTH:
            return True
        return False

    def climb(self, peak: BasePeak) -> None:
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2

        else:
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)
