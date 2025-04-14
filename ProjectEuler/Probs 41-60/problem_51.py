"""By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime. By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family,
is the smallest prime with this property. Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part of an eight prime value family."""

import itertools
from sympy import isprime

def generate_patterns(num_str):
    patterns = []
    length = len(num_str)
    for i in range(1, length):
        for indexes in itertools.combinations(range(length), i):
            pattern = list(num_str)
            chars = [pattern[i] for i in indexes]
            if len(set(chars)) == 1:
                for i in indexes:
                    pattern[i] = '*'
                    patterns.append(''.join(pattern))
    return patterns

def prime_family_count(pattern):
    primes = []
    for d in '0123456789':
        if pattern[0] == '*' and d == '0':
            continue
        candidate = int(pattern.replace('*', d))
        if isprime(candidate):
            primes.append(candidate)
    return primes

def find_smallest_prime_in_family(target_family_size):
    prime = 11
    while True:
        if isprime(prime):
            patterns = generate_patterns(str(prime))
            for pattern in patterns:
                family = prime_family_count(pattern)
                if len(family) == target_family_size:
                    return min(family)
        prime += 2

print(find_smallest_prime_in_family(8))