"""Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

fifth_powers = []

for i in range(1, 2_000_000):
    number = 0
    for j in str(i):
        j = int(j) ** 5
        number += j
    if number == i:
        fifth_powers.append(i)

print(fifth_powers)
print(sum(fifth_powers))
