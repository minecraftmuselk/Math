"""What is the index of the first term in the Fibonacci sequence to contain 1000 digits"""

a = 1
b = 1

fib_seq = [a, b]
for i in range(1, 100_000):
    next_number = fib_seq[-1] + fib_seq[-2]
    fib_seq.append(next_number)

for i in fib_seq:
    if len(str(i)) == 999:
        my_num = fib_seq.index(i)
        print(my_num)
        break

print(fib_seq)
