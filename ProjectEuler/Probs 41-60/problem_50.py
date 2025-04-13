"""The prime 41 can be written as the sum of six consecutive primes. This is the longest sum of consecutive primes that
adds to a prime below one-hundred. The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953. Which prime, below one-million, can be written as the sum of the most
consecutive primes?"""

from basic_functions import is_prime

LIMIT = 1_000_001
primes = [i for i in range(2, LIMIT) if is_prime(i)]
prime_set = set(primes)

max_length = 0
max_prime = 0

cumulative = [0]
for p in primes:
    cumulative.append(cumulative[-1] + p)

# Try all combinations of prime sums
for i in range(len(cumulative)):
    for j in range(i - (max_length + 1), -1, -1):  # only try longer sequences
        total = cumulative[i] - cumulative[j]
        if total > LIMIT:
            break
        if total in prime_set:
            max_length = i - j
            max_prime = total

print(f"Longest consecutive prime sum: {max_prime} with {max_length} terms")