"""Find the next triangle number that is also pentagonal and hexagonal."""

def is_triangle(x):
    n = (-1 + (1 + 8 * x) ** 0.5) / 2
    return n.is_integer()


def is_pentagon(y):
    n = (1 + (1 + 24 * y) ** 0.5) / 6
    return n.is_integer()


def is_hexagon(z):
    n = (1 + (1 + 8 * z) ** 0.5) / 4
    return n.is_integer()


def main():
    n = 144
    while True:
        hexagonal_number = n * (2 * n - 1)
        if hexagonal_number > 40756 and is_pentagon(hexagonal_number) and is_triangle(hexagonal_number):
            return hexagonal_number
        n += 1


print(main())
