"""For which value of p <= 1000, is the number of solutions maximised?"""

results = []


def count_pythagorean_triples(perimeter):
    count = 0
    for i in range(1, perimeter):
        for j in range(i, perimeter - i):
            k = perimeter - i - j
            if k > j and i**2 + j**2 == k**2:
                count += 1
    return count


def main():
    max_triples = 0
    best_perimeter = 0
    for p in range(1, 1001):
        triples_count = count_pythagorean_triples(p)
        if triples_count > max_triples:
            max_triples = triples_count
            best_perimeter = p
    return best_perimeter


print(main())
