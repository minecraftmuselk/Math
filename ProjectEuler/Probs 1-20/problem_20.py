"""Find the sum of the digits in the number 100!"""

import math

facts = []
for i in range(1, 101):
    facts.append(i)

factorial = math.prod(facts)
factorial = str(factorial)
add = 0

for i in factorial:
    i = int(i)
    add += i

print(factorial)
print(add)
