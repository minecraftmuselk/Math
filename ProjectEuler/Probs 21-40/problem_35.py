"""How many circular primes are there below one million?"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def rotate_number(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def is_circular_prime(n):
    rotations = rotate_number(n)
    return all(is_prime(rot) for rot in rotations)


circular_primes = [n for n in range(1, 1000000) if is_circular_prime(n)]

print(len(circular_primes))
