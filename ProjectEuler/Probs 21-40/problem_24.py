"""What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

from itertools import permutations

perms = []

perm = sorted(''.join(chars) for chars in permutations('0123456789'))
for x in perm:
    perms.append(x)

print(perms[999999])
