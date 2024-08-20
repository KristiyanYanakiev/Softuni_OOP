from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):

    PROTECTION = 90
    PRICE = 25.0

    def __init__(self):
        super().__init__(self.PROTECTION, self.PRICE)

    def increase_price(self) -> None:
        self.price += 0.1 * self.price




