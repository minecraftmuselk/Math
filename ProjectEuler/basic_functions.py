"""File to get basic functions of mathematics"""


def rotate_number(k):
    s = str(k)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def convert_to_binary(b):
    return bin(b)[2:]


# Checking if a number has certain property

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
