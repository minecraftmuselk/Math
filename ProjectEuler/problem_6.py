num = []
for i in range(1, 101):
    i = i ** 2
    num.append(i)

num2 = []
for i in range(1, 101):
    num2.append(i)

sum6 = sum(num)
square = sum(num2) ** 2
print(square - sum6)
