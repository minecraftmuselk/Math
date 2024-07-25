from itertools import permutations

perms = []

perm = sorted(''.join(chars) for chars in permutations('0123456789'))
for x in perm:
    perms.append(x)

print(perms[999999])
