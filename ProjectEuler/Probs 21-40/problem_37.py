"""Find the sum of the only eleven primes that are both truncatable from left to right and right to left."""

primes = []


def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_truncatable_primes(n):
    if not is_prime(n):
        return False
    n = str(n)
    for i in range(1, len(n)):
        j = int(n[i:])
        k = int(n[:i])
        if not is_prime(k) or not is_prime(j):
            return False
    return True


def main():
    for i in range(11, 1_000_000):
        if is_truncatable_primes(i):
            primes.append(i)


main()

print(primes)
print(sum(primes))
