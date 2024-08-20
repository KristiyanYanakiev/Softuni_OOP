from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):

    AMUNITIONS = 100

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.AMUNITIONS)

    def attack(self) -> None:
        self.ammunition -= 25
        if self.ammunition < 0:
            self.ammunition = 0
