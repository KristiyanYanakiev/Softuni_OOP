from abc import ABC, abstractmethod


class Playing_class(ABC):

    @abstractmethod
    def play(self):
        pass


class Guitar(Playing_class):

    def __init__(self, play_text: str):
        self.play_text = play_text

    def play(self):
        return f"{self.play_text}"

guitar = Guitar("text")

print(guitar.play_text)
print(guitar.play())
