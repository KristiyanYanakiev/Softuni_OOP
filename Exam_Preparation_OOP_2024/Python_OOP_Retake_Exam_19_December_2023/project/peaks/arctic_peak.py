from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    def __init__(self, name: str, elevation: int):

        super().__init__(name, elevation)
        self.difficulty_level = self.calculate_difficulty_level()

    RECOMMENDED_GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        if self.elevation > 3000:
            return "Extreme"

        if 2000 <= self.elevation <= 3000:
            return "Advanced"

    def get_recommended_gear(self):
        return self.RECOMMENDED_GEAR
