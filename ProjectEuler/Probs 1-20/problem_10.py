"""Find the sum of all the primes below two million"""

prime_numbers = []
for num in range(1, 2_000_001):
    for i in range(1, num):
        if (num % i) == 0:
            break
    else:
        prime_numbers.append(num)

print(sum(prime_numbers))
