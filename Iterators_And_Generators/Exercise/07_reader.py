def read_next(*args):

    for sequence in args:
        # index = 0
        # while index < len(sequence):
        #     if isinstance(sequence, dict):
        #         sequence = list(sequence.keys())
        #     yield sequence[index]
        #     index += 1

        # for el in sequence:
        #     yield el

        yield from sequence

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
