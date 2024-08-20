from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    def multiply(*args) -> int:
        return reduce(lambda x, y: x * y, args)

    def divide(*args) -> float:
        return reduce(lambda x, y: x / y, args)

    def subtract(*args) -> int:
        return reduce(lambda x, y: x - y, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))

