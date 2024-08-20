from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):

        royalships_count = len([s for s in self.ships if isinstance(s, RoyalBattleship)])
        ships_info = self.get_ships()
        ship_names = [s.name for s in ships_info]

        result = []

        result.append(f"@Pirate Zone Statistics@\nCode: {self.code}; Volume: {self.volume}\n"
                      f"Battleships currently in the Pirate Zone: {len(self.ships)}, "
                      f"{royalships_count} out of them are Royal Battleships.")

        if self.ships:
            result.append(f"#{', '.join(ship_names)}#")

        return '\n'.join(result)
