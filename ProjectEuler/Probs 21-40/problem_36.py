"""Find the sum of all numbers, less than one million, which are palindromic in base 10 and 2"""

def convert_to_binary(n):
    return bin(n)[2:]


def is_palindrome(n):
    n = str(n)
    reverse = n[::-1]
    if reverse == n:
        return True
    else:
        return False


def main():
    palindromic = []
    for i in range(1, 1_000_001):
        b = convert_to_binary(i)
        if is_palindrome(i) and is_palindrome(b):
            palindromic.append(i)
        else:
            pass
    return sum(palindromic)


print(main())
