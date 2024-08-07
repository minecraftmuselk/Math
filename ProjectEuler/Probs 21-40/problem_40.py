irrational_decimal = ''

for i in range(1, 1_000_000):
    i = str(i)
    irrational_decimal = irrational_decimal + i

d1 = irrational_decimal[0]
d2 = irrational_decimal[9]
d3 = irrational_decimal[99]
d4 = irrational_decimal[999]
d5 = irrational_decimal[9999]
d6 = irrational_decimal[99999]
d7 = irrational_decimal[999999]

answer = int(d1) * int(d2) * int(d3) * int(d4) * int(d5) * int(d6) * int(d7)
print(answer)
