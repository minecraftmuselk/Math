"""What is the largest n-digit pandigital prime that exists?"""

from itertools import permutations


def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def largest_pandigital_prime():
    # Only 7-digit and 4-digit pandigital numbers can be prime.
    for n in range(7, 0, -1):  # Start with the largest n and go downwards.
        pandigital_numbers = [''.join(p) for p in permutations('123456789'[:n])]
        pandigital_numbers = sorted(map(int, pandigital_numbers), reverse=True)
        for num in pandigital_numbers:
            if is_prime(num):
                return num
    return None


print(largest_pandigital_prime())
