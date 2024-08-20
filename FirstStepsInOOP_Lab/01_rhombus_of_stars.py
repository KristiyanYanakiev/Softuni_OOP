def print_row(size, row):
    print(f"{' ' * (size - row)}{'* ' * row}")


def print_upper_part_of_rhombus(size):
    for row in range(1, size + 1):
        print_row(size, row)


def print_lower_part_of_rhombus(size):
    for row in range(size - 1, 0, -1):
        print_row(size, row)


def draw_rhombus(size):
    print_upper_part_of_rhombus(size)
    print_lower_part_of_rhombus(size)


n = int(input())

draw_rhombus(n)