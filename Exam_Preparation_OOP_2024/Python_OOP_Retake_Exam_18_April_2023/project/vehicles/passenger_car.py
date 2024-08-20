from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    max_mileage = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.max_mileage)

    def drive(self, mileage: float):

        calculated_value = int((self.max_mileage / mileage) * 100)
        calculated_value = calculated_value / 100

        self.battery_level -= self.battery_level * calculated_value


