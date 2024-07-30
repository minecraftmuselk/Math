"""If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""

from fractions import Fraction


def find_curious_fractions():
    curious_fractions = []

    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):  # denominator must be greater than numerator
            num_str, denom_str = str(numerator), str(denominator)

            # Check if there are any common digits (excluding '0')
            common_digits = set(num_str) & set(denom_str)
            if common_digits and '0' not in common_digits:
                common_digit = common_digits.pop()
                new_num_str = num_str.replace(common_digit, '', 1)
                new_denom_str = denom_str.replace(common_digit, '', 1)

                if new_num_str != '' and new_denom_str != '':
                    new_num, new_denom = int(new_num_str), int(new_denom_str)
                    if new_denom != 0 and Fraction(numerator, denominator) == Fraction(new_num, new_denom):
                        curious_fractions.append(Fraction(numerator, denominator))

    # Calculate the product of all curious fractions
    product = Fraction(1, 1)
    for frac in curious_fractions:
        product *= frac

    return product.denominator


print(find_curious_fractions())
