"""Find the pair of pentagonal numbers, PJ and PD , for which their sum and difference are pentagonal and D is
minimised; what is the value of?"""


def is_pentagonal(x):
    # Inverse of the pentagonal number formula: n(3n-1)/2
    n = (1 + (1 + 24 * x) ** 0.5) / 6
    return n.is_integer()


def main():
    pentagonal_numbers = set()  # Use a set for O(1) lookups
    pair_pentagons = []
    for i in range(1, 10000):
        pentagonal_i = i * (3 * i - 1) // 2
        pentagonal_numbers.add(pentagonal_i)
        for pentagonal_j in pentagonal_numbers:
            if pentagonal_i != pentagonal_j:
                if is_pentagonal(pentagonal_i + pentagonal_j) and is_pentagonal(abs(pentagonal_i - pentagonal_j)):
                    pair_pentagons.append((pentagonal_i, pentagonal_j))
                    print(f"Pair found: {pentagonal_i}, {pentagonal_j}")
                    return abs(pentagonal_i - pentagonal_j)


result = main()
print(f"Smallest difference: {result}")
