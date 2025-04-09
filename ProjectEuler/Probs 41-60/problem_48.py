"""Find the last ten digits of the series, 1^1 + ... 1000^1000"""

num = 0

for i in range(1001):
    num += i**i

print(num)
