found = False
n = 1
while not found:
    found = True
    for i in range(1, 21):
        if n % i != 0:
            found = False
    if found:
        print(i)
    n += 1

print(n)