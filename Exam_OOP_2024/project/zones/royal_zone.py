from project.battleships.pirate_battleship import PirateBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self) -> str:

        pirate_ships_len = len([sh for sh in self.ships if isinstance(sh, PirateBattleship)])
        ships_info = self.get_ships()
        ship_names = [s.name for s in ships_info]

        result = []

        result.append(f"@Royal Zone Statistics@\nCode: {self.code}; Volume: {self.volume}\n"
                      f"Battleships currently in the Royal Zone: {len(self.ships)}, "
                      f"{pirate_ships_len} out of them are Pirate Battleships.")

        if self.ships:
            result.append(f"#{', '.join(ship_names)}#")

        return '\n'.join(result)
