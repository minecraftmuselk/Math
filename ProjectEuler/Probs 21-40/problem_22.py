with open('0022_names.txt', 'r') as file:
    content = file.read()

name_list = content.replace('"', '').split(',')
name_list.sort()

d = dict()
j = 1
for i in range(ord('A'), ord('Z')+1):
    d[chr(i)] = j
    j += 1

tot = 0
l = []
i = 0
for i in range(6000):
    for s in name_list[i]:
        if s == '"':
            continue
        else:
            tot += d[s]

    p = (i + 1) * tot
    l.append(p)

    if (name_list[i] == '"COLIN"'):
        print(name_list[i], " i= ", i)
        print("p= ", p, " tot= ", tot)
        print(name_list[i], "  ", l[i])

    tot = p = 0

    p = 0
    print("len(l) = ", len(l))
    for i in range(len(l)):
        p += l[i]
    print("total score= ", p)
print(name_list)
print(d)
