import sympy


def find_max_primes():
    max_primes = 0
    product = 0

    for a in range(-999, 1000):
        for b in sympy.primerange(-1000, 1001):
            n = 0
            while True:
                quadratic_value = n * n + a * n + b
                if sympy.isprime(quadratic_value):
                    n += 1
                else:
                    break

            if n > max_primes:
                max_primes = n
                product = a * b

    return product


result = find_max_primes()
print(result)
