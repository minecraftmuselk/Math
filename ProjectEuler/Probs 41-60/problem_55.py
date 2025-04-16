"""If we take 47 reverse and add 47+74=121 which is palindromic. Although no one has proved it yet, it is thought that
some numbers, like never produce a palindrome. A number that never forms a palindrome through the reverse and add
process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem,
we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below
ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the
computing power that exists, has managed so far to map it to a palindrome.

How many Lychrel numbers are there below ten-thousand?"""

from basic_functions import rotate_number, is_palindrome
lns = []
for i in range(1, 10_001):
    n = i
    found_palindrome = False
    for _ in range(1, 51):
        n = n + rotate_number(n)
        if is_palindrome(n):
            found_palindrome = True
            break

    if not is_palindrome(n):
        lns.append(i)
print(len(lns))