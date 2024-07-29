"""Find the value of d<1000 for which 1/d contains the longest recurring cycle in its decimal fraction part"""

def recurring_cycle_length(d):
    remainders = {}
    value = 1
    position = 0

    while value != 0 and value not in remainders:
        remainders[value] = position
        value *= 10
        value %= d
        position += 1

    if value != 0:
        return position - remainders[value]
    else:
        return 0

max_length = 0
number = 0

for d in range(1, 1000):
    cycle_length = recurring_cycle_length(d)
    if cycle_length > max_length:
        max_length = cycle_length
        number = d

print(f"The number with the longest recurring cycle is {number} with a cycle length of {max_length}.")