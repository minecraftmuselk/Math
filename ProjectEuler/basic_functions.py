"""File to get basic functions of mathematics"""
import itertools


def rotate_number(k):
    s = str(k)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def convert_to_binary(b):
    return bin(b)[2:]


"""Checking if a number has certain property"""


def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(m):
    m = str(m)
    reverse = m[::-1]
    if reverse == m:
        return True
    else:
        return False


def is_9_pandigital(a):
    a = str(a)
    digits = set(a)
    return len(a) == 9 and digits == set('123456789')


def is_pandigital(e):
    e = str(e)
    digits = set(e)
    number = ''
    for i in range(1, len(e)+1):
        number += str(i)
    return digits == set(number)


def is_pythagorean(a, b, c):
    return (a ** 2) + (b ** 2) == (c ** 2)


def has_substring_divisibility_property(n):
    return (int(n[1:4]) % 2 == 0 and
            int(n[2:5]) % 3 == 0 and
            int(n[3:6]) % 5 == 0 and
            int(n[4:7]) % 7 == 0 and
            int(n[5:8]) % 11 == 0 and
            int(n[6:9]) % 13 == 0 and
            int(n[7:10]) % 17 == 0)


def is_triangle(x):
    n = (-1 + (1 + 8 * x) ** 0.5) / 2
    return n.is_integer()


def is_pentagon(y):
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()


def pandigitals():
    pans = []
    for perm in itertools.permutations('0123456789'):
        num = ''.join(perm)
        pans.append(perm)


def pentagonals():
    pentagonal_numbers = []
    for i in range(1, 11):
        i = (i * ((3 * i) - 1)) / 2
        pentagonal_numbers.append(i)
    return pentagonal_numbers


"""Files"""


def dictionary_for_word_value():
    d = dict()
    j = 1
    for i in range(ord('A'), ord('Z') + 1):
        d[chr(i)] = j
        j += 1


def get_word_value(word):
    d = dict()
    j = 1
    for i in range(ord('A'), ord('Z') + 1):
        d[chr(i)] = j
        j += 1
    word_value = 0
    word = word.upper()
    for letter in word:
        word_value += d[letter]
    return word_value


def write_triangle_numbers():
    triangle_numbers = []
    for i in range(1, 10_000):
        i = (i / 2) * (i + 1)
        i = int(i)
        triangle_numbers.append(i)
    return triangle_numbers


h = '54123'
print(is_pandigital(h))
