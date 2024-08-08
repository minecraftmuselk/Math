"""Find the sum of all 0 to 9 pandigital numbers with this property."""

import itertools


def is_10_pandigital(a):
    a = str(a)
    digits = set(a)
    return len(a) == 10 and digits == set('0123456789')


def has_property(n):
    return (int(n[1:4]) % 2 == 0 and
            int(n[2:5]) % 3 == 0 and
            int(n[3:6]) % 5 == 0 and
            int(n[4:7]) % 7 == 0 and
            int(n[5:8]) % 11 == 0 and
            int(n[6:9]) % 13 == 0 and
            int(n[7:10]) % 17 == 0)


def main():
    pandigital_numbers_property = []
    for perm in itertools.permutations('0123456789'):
        num = ''.join(perm)
        if has_property(num):
            pandigital_numbers_property.append(int(num))
    return sum(pandigital_numbers_property)


print(main())
