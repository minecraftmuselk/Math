"""What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"""

import math


def sieve(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for start in range(2, limit + 1):
        if sieve[start]:
            primes.append(start)
            for i in range(start * start, limit + 1, start):
                sieve[i] = False

    return primes


def is_goldbach_exception(n, primes):
    for prime in primes:
        if prime >= n:
            break
        remainder = n - prime
        if remainder % 2 == 0:
            square = remainder // 2
            if math.isqrt(square) ** 2 == square:
                return False
    return True


def find_smallest_odd_composite_exception(limit):
    primes = sieve(limit)
    for n in range(9, limit, 2):  # Start from 9, the first odd composite number
        if n not in primes and is_goldbach_exception(n, primes):
            return n


print(find_smallest_odd_composite_exception(10000))