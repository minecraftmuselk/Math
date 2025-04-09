"""The arithmetic sequence, 1487,4817,8147 in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

What 12-digit number do you form by concatenating the three terms in this sequence?"""

from basic_functions import is_prime
from itertools import permutations

primes = [i for i in range(1000, 10000) if is_prime(i)]

for p in primes:
    for d in range(1, 4500):
        p2 = p + d
        p3 = p + 2*d
        if p3 >= 10000:
            continue
        if is_prime(p2) and is_prime(p3):
            if sorted(str(p)) == sorted(str(p2)) == sorted(str(p3)):
                if p != 1487:
                    result = f"{p}{p2}{p3}"
                    print(result)