"""Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

If one complete new layer is wrapped around the spiral above, a square spiral with side length will be formed.
If this process is continued, what is the side length of the square spiral for which the ratio of primes along
both diagonals first falls below?"""

from sympy import isprime

side_length = 1
prime_count = 0
diag_count = 1  # starts with just the center 1

while True:
    side_length += 2  # side length increases by 2 for each layer
    square = side_length ** 2
    corners = [square - i * (side_length - 1) for i in range(4)]

    # Check primes in corners
    prime_count += sum(1 for corner in corners if isprime(corner))
    diag_count += 4

    if prime_count / diag_count < 0.10:
        break

print(f"Answer: {side_length}")