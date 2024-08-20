from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    valid_vehicles_mapper = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        for u in self.users:
            if u.driving_license_number == driving_license_number:
                break
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:

        if vehicle_type not in self.valid_vehicles_mapper:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for v in self.vehicles:
            if v.license_plate_number == license_plate_number:
                break
            return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.valid_vehicles_mapper[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float) -> str:

        for r in self.routes:
            if [r.start_point, r.end_point, r.length] == [start_point, end_point, length]:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if [r.start_point, r.end_point] == [start_point, end_point] and r.length < length:
                return "{start_point}/{end_point} shorter route had already been added to our platform."

            if [r.start_point, r.end_point] == [start_point, end_point] and r.length > length:
                r.is_locked = True

        route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        vehicle.drive(route.length)
        return str(vehicle)

    def repair_vehicles(self, count: int) -> str:

        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        ordered_damaged_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))

        vehicles_to_repair = []

        for index in range(count):
            vehicles_to_repair.append(ordered_damaged_vehicles[index])

        for v in vehicles_to_repair:
            v.is_damaged = False
            v.recharge()

        return f"{len(vehicles_to_repair)} vehicles were successfully repaired!"

    def users_report(self) -> str:

        sorted_users = sorted(self.users, key=lambda u: - u.rating)

        result = ["*** E-Drive-Rent ***"]
        for u in sorted_users:
            result.append(f"{str(u)}")

        return "\n".join(result)















