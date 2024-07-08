"""What is the 10,001st prime number?"""

prime_numbers = []

for num in range(1, 200000):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        prime_numbers.append(num)

print(prime_numbers)
print(prime_numbers[10_002])
