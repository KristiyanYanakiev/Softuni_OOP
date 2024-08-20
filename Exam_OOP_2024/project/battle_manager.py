from typing import List

from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    valid_zone_types_mapper = {
        "RoyalZone": RoyalZone,
        "PirateZone": PirateZone
    }

    valid_ship_types_mapper = {
        "RoyalBattleship": RoyalBattleship,
        "PirateBattleship": PirateBattleship
    }

    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str) -> Exception or str:

        if zone_type not in self.valid_zone_types_mapper:
            raise Exception("Invalid zone type!")

        try:
            zone = next(filter(lambda z: z.code == zone_code, self.zones))
            raise Exception("Zone already exists!")
        except StopIteration:
            created_zone = self.valid_zone_types_mapper[zone_type](zone_code)
            self.zones.append(created_zone)

            return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int) -> Exception or str:

        if ship_type not in self.valid_ship_types_mapper:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        created_ship = self.valid_ship_types_mapper[ship_type](name, health, hit_strength)
        self.ships.append(created_ship)

        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship) -> str:

        if zone.volume == 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health == 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if isinstance(ship, PirateBattleship) and isinstance(zone, RoyalZone):
            ship.is_under_attack = True
        elif isinstance(ship, RoyalBattleship) and isinstance(zone, PirateZone):
            ship.is_under_attack = True
        elif isinstance(ship, PirateBattleship) and isinstance(zone, PirateZone):
            ship.is_attacking = True
        elif isinstance(ship, RoyalBattleship) and isinstance(zone, RoyalZone):
            ship.is_attacking = True


        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):

        try:
            ship = next(filter(lambda s: s.name == ship_name, self.ships))
        except StopIteration:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)

        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone) -> str:

        attackers_ships = [s for s in zone.ships if s.is_attacking]
        under_attack_ships = [s for s in zone.ships if s.is_under_attack]

        if not all([len(attackers_ships) >= 1, len(under_attack_ships) >= 1]):
            return "Not enough participants. The battle is canceled."

        if isinstance(zone, RoyalZone):
            corresponding_ships = [s for s in zone.ships if isinstance(s, RoyalBattleship)]
            non_corresponding_ships = [s for s in zone.ships if isinstance(s, PirateBattleship)]
        else:
            corresponding_ships = [s for s in zone.ships if isinstance(s, PirateBattleship)]
            non_corresponding_ships = [s for s in zone.ships if isinstance(s, RoyalBattleship)]

        attacker = sorted(corresponding_ships, key=lambda s: s.hit_strength)[0]
        oponent = sorted(non_corresponding_ships, key=lambda s: s.health)[0]

        attacker.attack()
        oponent.take_damage(attacker)

        if oponent.health == 0:
            zone.ships.remove(oponent)
            self.ships.remove(oponent)

            return f"{oponent.name} lost the battle and was sunk."

        if attacker.ammunition == 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)

            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self) -> str:

        result = []

        available_ships = [s.name for s in self.ships if s.is_available]

        result.append(f"Available Battleships: {len(available_ships)}")

        if available_ships:
            result.append(f"#{', '.join(available_ships)}#")

        sorted_zones = sorted(self.zones, key=lambda z: z.code)

        result.append(f"***Zones Statistics:***\nTotal Zones: {len(self.zones)}")

        for zone in sorted_zones:
            result.append(zone.zone_info())

        return '\n'.join(result)
