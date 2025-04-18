"""There are exactly ten ways of selecting three from five 12345: 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, (5 3) = 10. In general, (n r) = n! / r!(n-r)!, where r <= n. It is not until
n = 23, that a value exceeds one-million: (23 10) = 1144066. How many, not necessarily distinct values of (n r) for
1 <= n <= 100, are greater than one-million?"""

import math

answer = []
for n in range(1, 101):
    for r in range(1, n):
        ways = math.comb(n, r)
        if ways > 1_000_000:
            answer.append(ways)

print(len(answer))