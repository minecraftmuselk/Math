"""What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
with (1, 2)?"""


def is_pandigital(n):
    n_str = str(n)
    return len(n_str) == 9 and set(n_str) == set('123456789')


def concatenated_product(integer, n):
    return ''.join(str(integer * i) for i in range(1, n + 1))


def find_largest_pandigital():
    largest_pandigital = 0

    for i in range(1, 10000):  # limit chosen based on problem analysis
        concatenated = ''
        n = 1
        while len(concatenated) < 9:
            concatenated += str(i * n)
            n += 1
        if len(concatenated) == 9 and is_pandigital(concatenated):
            largest_pandigital = max(largest_pandigital, int(concatenated))

    return largest_pandigital


# Find the largest 1 to 9 pandigital number
result = find_largest_pandigital()
print(result)
