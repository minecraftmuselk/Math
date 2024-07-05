def get_triplet():
    for c in range(2, 1000):
        for b in range(2, c):
            a = 1000 - c - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


if __name__ == '__main__':
    print(get_triplet())
