"""Find the sum of all numbers which are equal to the sum of the factorial of their digits."""
import math


def sum_of_digit_factorials(n):
    return sum(math.factorial(int(digit)) for digit in str(n))


def find_curious_number():
    limit = 7 * math.factorial(9)
    curious_numbers = []

    for i in range(10, limit):
        if i == sum_of_digit_factorials(i):
            curious_numbers.append(i)

    return sum(curious_numbers)


print(find_curious_number())
