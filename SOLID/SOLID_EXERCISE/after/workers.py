from abc import ABC, abstractmethod


class BaseWorker(ABC):

    @abstractmethod
    def work(self):
        pass

class Worker(BaseWorker):

    def work(self) -> None:
        print("I'm working!!")


class SuperWorker(BaseWorker):

    def work(self):
        print("I work very hard!!!")


class RobotWorker(BaseWorker):
    def work(self):
        print("I work very ultra hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), f'`worker` must be of type {BaseWorker}'

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()



worker = Worker()

manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
manager.set_worker(super_worker)
manager.manage()
