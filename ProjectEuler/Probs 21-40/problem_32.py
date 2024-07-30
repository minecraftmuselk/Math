def is_pandigital(n):
    digits = sorted(str(n))
    return digits == ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def pandigital_products():
    products = set()
    for a in range(1, 100):
        for b in range(a, 10000):  # b is up to 4 digits
            product = a * b
            identity = str(a) + str(b) + str(product)
            if len(identity) > 9:
                break
            if is_pandigital(identity):
                products.add(product)
    return sum(products)


print(pandigital_products())
