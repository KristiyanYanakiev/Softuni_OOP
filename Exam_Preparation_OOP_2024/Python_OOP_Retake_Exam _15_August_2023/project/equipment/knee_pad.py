from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):

    PROTECTION = 120
    PRICE = 15.0

    def __init__(self):
        super().__init__(self.PROTECTION, self.PRICE)

    def increase_price(self) -> None:
        self.price += 0.2 * self.price
