"""What is the value of the first triangle number to have over five hundred divisors?"""

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2  # i and n/i are both divisors
        if i * i == n:
            count -= 1  # Correct the count if n is a perfect square
    return count


def highly_divisible_triangular_number(min_divisors):
    n = 1
    while True:
        triangular_number = n * (n + 1) // 2
        if count_divisors(triangular_number) > min_divisors:
            return triangular_number
        n += 1


# Example usage
min_divisors = 500
result = highly_divisible_triangular_number(min_divisors)
print(f"The first triangular number with more than {min_divisors} divisors is {result}")