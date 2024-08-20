def genrange(start: int, end: int):
    while start <= end:
        yield start
        start += 1


# class generator_range:
#     def __init__(self, start: int, end: int):
#         self.start = start - 1
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start == self.end:
#             raise StopIteration
#
#         self.start += 1
#         return self.start


print(list(genrange(1, 10)))

