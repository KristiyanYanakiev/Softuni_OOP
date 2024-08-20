from abc import ABC, abstractmethod


class Working(ABC):
    @abstractmethod
    def work(self):
        pass


class Eating:
    @abstractmethod
    def eat(self):
        pass


class Worker(Working, Eating):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")


class SuperWorker(Working, Eating):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")


class BaseManager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        ...


class WorkingManager(BaseManager):

    def set_worker(self, worker):
        assert isinstance(worker, Working), f"`worker` must be of type {Working}"

        self.worker = worker

    def manage(self):
        self.worker.work()


class EatingManager(BaseManager, Eating):

    def set_worker(self, worker):
        assert isinstance(worker, Eating), f"`worker` must be of type {Eating}"

        self.worker = worker

    def manage(self):
        self.worker.eat()


class RobotWorker(Working):

    def work(self):
        print("I'm a robot. I'm working....")

class LazyWorker(Eating):

    def eat(self):
        print("I'm a lazy worker. I'm only eating...")


worker = Worker()
super_worker = SuperWorker()
robot_worker = RobotWorker()
lazy_worker = LazyWorker()

working_manager = WorkingManager()
eating_manager = EatingManager()

robot_worker.work()
working_manager.set_worker(robot_worker)
working_manager.worker.work()

eating_manager.set_worker(lazy_worker)
eating_manager.worker.eat()
