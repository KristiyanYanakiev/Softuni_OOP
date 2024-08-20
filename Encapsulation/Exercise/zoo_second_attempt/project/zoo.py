from typing import List

from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price) -> str:

        if self.__budget >= price and self.__animal_capacity > 0:

            self.animals.append(animal)

            self.__budget -= price

            self.__animal_capacity -= 1

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price and self.__animal_capacity > 0:

            return "Not enough budget"

        return "Not enough space for animal"



    def hire_worker(self, worker: Worker) -> str:

        if self.__workers_capacity > 0:

            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            self.__workers_capacity += 1
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        salaries_to_pay = sum([w.salary for w in self.workers])
        if salaries_to_pay <= self.__budget:
            self.__budget -= salaries_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        money_for_animal_care = sum([a.money_for_care for a in self.animals])
        if money_for_animal_care <= self.__budget:
            self.__budget -= money_for_animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:

        lion_counter = 0
        lion_string = ""
        tiger_counter = 0
        tiger_string = ""
        cheetah_counter = 0
        cheetah_string = ""

        for a in self.animals:
            if isinstance(a, Lion):
                lion_counter += 1
                lion_string += f"{a}\n"
            elif isinstance(a, Tiger):
                tiger_counter += 1
                tiger_string += f"{a}\n"
            elif isinstance(a, Cheetah):
                cheetah_counter += 1
                cheetah_string += f"{a}\n"

        res = ( f"You have {len(self.animals)} animals\n"
                f"----- {lion_counter} Lions:\n"
                f"{lion_string}"
                f"----- {tiger_counter} Tigers:\n"
                f"{tiger_string}"
                f"----- {cheetah_counter} Cheetahs:\n"
                f"{cheetah_string}")

        return res[:-1]

    def workers_status(self) -> str:

        keepers_counter = 0
        keepers_string = ""
        caretakers_counter = 0
        caretakers_string = ""
        vets_counter = 0
        vets_string = ""

        for w in self.workers:
            if isinstance(w, Keeper):
                keepers_counter += 1
                keepers_string += f"{w}\n"
            elif isinstance(w, Caretaker):
                caretakers_counter += 1
                caretakers_string += f"{w}\n"
            elif isinstance(w, Vet):
                vets_counter += 1
                vets_string += f"{w}\n"

        res = (f"You have {len(self.workers)} workers\n"
               f"----- {keepers_counter} Keepers:\n"
               f"{keepers_string}"
               f"----- {caretakers_counter} Caretakers:\n"
               f"{caretakers_string}"
               f"----- {vets_counter} Vets:\n"
               f"{vets_string}")

        return res[:-1]
