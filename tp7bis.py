from tp7 import Fraction


def main():
    # Création de deux fractions
    f1 = Fraction(3, 4)
    f2 = Fraction(2, 3)

    print(f1)  # Outputs: 3/4
    print(f2)  # Outputs: 2/3

    print(f1.numerator)  # Outputs: 3
    print(f1.denominator)  # Outputs: 4

    print(f1.as_mixed_number())  # Outputs: 3/4

    print(f1 + f2)  # Outputs: 17/12
    print(f1 - f2)  # Outputs: 1/12
    print(f1 * f2)  # Outputs: 1/2
    print(f1 / f2)  # Outputs: 9/8
    print(f1 ** 2)  # Outputs: 9/16

    print(f1 == f2)  # Outputs: False

    print(float(f1))  # Outputs: 0.75

    print(f1.is_zero)  # Outputs: False
    print(f1.is_integer)  # Outputs: False
    print(f1.is_proper)  # Outputs: True
    print(f1.is_unit)  # Outputs: False
    print(f1.is_adjacent_to(f2))  # Outputs: False


if __name__ == '__main__':
    main()
