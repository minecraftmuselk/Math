"""Find the sum of the only eleven primes that are both truncatable from left to right and right to left."""

primes = []


def is_prime(n):
    n = int(n)
    if n <= 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_truncatable_primes(n):
    n = str(n)
    end = -1
    start = 1
    while is_prime(n):
        j = n[:end]
        k = n[start:]
        while len(j) >= 1 and len(k) >= 1:
            while is_prime(j) and is_prime(k):
                return True
            else:
                return False
        start += 1
        end -= 1

    return False


def main():
    for i in range(11, 100_000):
        if is_truncatable_primes(i):
            primes.append(i)


main()

print(primes)
