"""It is possible to show that the square root of two can be expressed as an infinite continued fraction. In the
first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?"""

from fractions import Fraction

answer = 0
n = 3
d = 2

for _ in range(1, 1001):
    if len(str(n)) > len(str(d)):
        answer += 1

    n, d = n + 2 * d, n + d

print(answer)