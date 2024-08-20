def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for num in integers():
            yield num / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

generator = solution()[2]()

for _ in range(10):
    print(next(generator))



