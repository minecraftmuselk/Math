def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def rotate_number(k):
    s = str(k)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def convert_to_binary(b):
    return bin(b)[2:]


def is_palindrome(m):
    m = str(m)
    reverse = m[::-1]
    if reverse == m:
        return True
    else:
        return False


def is_pandigital(a):
    a = str(a)
    digits = set(a)
    return len(a) == 9 and digits == set('123456789')


h = '123456789'

print(is_pandigital(9862457123))
