from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    valid_services_mapper = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    valid_robots_mapper = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str) -> str or Exception:
        if service_type not in self.valid_services_mapper:
            raise Exception("Invalid service type!")

        service = self.valid_services_mapper[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str or Exception:
        if robot_type not in self.valid_robots_mapper:
            raise Exception("Invalid robot type!")

        robot = self.valid_robots_mapper[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str or Exception:

        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]

        if isinstance(robot, MaleRobot) and isinstance(service, MainService):
            if service.capacity > len(service.robots):
                self.robots.remove(robot)
                service.robots.append(robot)
                return f"Successfully added {robot_name} to {service_name}."
            raise Exception("Not enough capacity for this robot!")

        if isinstance(robot, FemaleRobot) and isinstance(service, SecondaryService):
            if service.capacity > len(service.robots):
                self.robots.remove(robot)
                service.robots.append(robot)
                return f"Successfully added {robot_name} to {service_name}."
            raise Exception("Not enough capacity for this robot!")

        return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str or Exception:

        service = [s for s in self.services if s.name == service_name][0]

        try:
            robot = [r for r in service.robots if r.name == robot_name][0]
        except IndexError:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = [s for s in self.services if s.name == service_name][0]
        number_of_robots_fed = 0
        for r in service.robots:
            r.eating()
            number_of_robots_fed += 1

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str) -> str:
        service = [s for s in self.services if s.name == service_name][0]
        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):

        return '\n'.join(service.details() for service in self.services)






