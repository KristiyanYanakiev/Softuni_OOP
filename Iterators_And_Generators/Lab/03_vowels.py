class vowels:

    def __init__(self, string: str):
        self.string = string
        self.vowels: list = [ch for ch in self.string if ch.lower() in "aeiuyo"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):

        if self.index == len(self.vowels) - 1:
            raise StopIteration
        self.index += 1
        return self.vowels[self.index]





my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

