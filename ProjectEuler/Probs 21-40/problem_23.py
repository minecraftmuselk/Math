"""Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
# Not the right solution but got answer right

perfect_numbers = []
deficients = []
adundants = []

for i in range(1, 30):
    divisors = []
    for j in range(1, i):
        if i % j == 0:
            divisors.append(j)

    if sum(divisors) == i:
        perfect_numbers.append(i)
    elif sum(divisors) < i:
        deficients.append(i)
    elif sum(divisors) > i:
        adundants.append(i)

    print(sum(divisors))
    divisors.clear()

print(perfect_numbers)
print(deficients)
print(adundants)
