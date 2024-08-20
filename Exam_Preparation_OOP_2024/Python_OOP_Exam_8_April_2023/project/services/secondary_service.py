from project.services.base_service import BaseService


class SecondaryService(BaseService):

    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        if self.robots:
            robots_names = ' '.join(r.name for r in self.robots)
        else:
            robots_names = "none"

        return f"{self.name} Secondary Service:\nRobots: {robots_names}"