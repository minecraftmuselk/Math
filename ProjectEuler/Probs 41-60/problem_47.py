"""Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers
?"""


def prime_factors_count(n):
    factors = set( )
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors.add(n)
            break
    return len(factors)


def find_consecutive_numbers_with_prime_factors(limit):
    consecutive_count = 0
    i = 2
    while True:
        if prime_factors_count(i) == 4:
            consecutive_count += 1
            if consecutive_count == 4:
                return i - 3  # First number in the sequence
        else:
            consecutive_count = 0
        i += 1


print(find_consecutive_numbers_with_prime_factors(4))
