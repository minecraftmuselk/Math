def is_prime(n):
    n = int(n)
    if n <= 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def rotate_number(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]


def convert_to_binary(n):
    return bin(n)[2:]


def is_palindrome(n):
    n = str(n)
    reverse = n[::-1]
    if reverse == n:
        return True
    else:
        return False

"""primes = []
for i in range(11, 100_000):
    if is_prime(i):
        primes.append(i)
    for k in primes:
        counter = -1
        while len(str(k)) > 2:
            k = str(k)
            j = k[:counter]
            counter -= 1
            if not is_prime(j):
                primes.remove(i)
                break"""
n = '113'
j = n[:-1]
k = n[1:]
print(j)
print(k)
print(len(j))
print(len(k))
print(is_prime(n))
print(is_prime(j))
print(is_prime(k))
