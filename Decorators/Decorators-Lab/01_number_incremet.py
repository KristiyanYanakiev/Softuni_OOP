from typing import List


def number_increment(numbers: List[int]):
    def increase():

        return [n + 1 for n in numbers]

    return increase()


print(number_increment([1, 2, 3]))