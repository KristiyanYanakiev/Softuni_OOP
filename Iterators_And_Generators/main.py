def from_one_generator():

    num: int = 1
    while True:
        yield num
        num += 1


my_generator = from_one_generator()

for _ in range(5):
    print(next(my_generator))


