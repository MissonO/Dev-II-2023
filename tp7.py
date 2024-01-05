class Fraction:
    def __init__(self, num=0, den=1):
        if den == 0:
            raise ValueError("Denominateur est zero")
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Pas des nombres entiers")
        self.num = num
        self.den = den

    @property
    def numerator(self):
        return self.num

    @property
    def denominator(self):
        return self.den

# ------------------ Textual representations ------------------

    def __str__(self):
        return f"{self.num}/{self.den}"

    def as_mixed_number(self):
        whole = self.num // self.den
        remainder = self.num % self.den
        return f"{whole} {Fraction(remainder, self.den)}" if whole != 0 else str(Fraction(remainder, self.den))

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Pas une fraction")
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Pas une fraction")
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Pas une fraction")
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Pas une fraction")
        if other.num == 0:
            raise ValueError("Cannot divide by zero")
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError("Pas un entier")
        num = self.num ** power
        den = self.den ** power
        return Fraction(num, den)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Pas une fraction")
        return self.num == other.num and self.den == other.den

    def __float__(self):
        if self.den == 0:
            raise ValueError("Denominateur est zero")
        return self.num / self.den

    def is_zero(self):
        return self.num == 0

    def is_integer(self):
        if not isinstance(self.num, int) or not isinstance(self.den, int):
            raise TypeError("Pas des nombres entiers")
        return self.den == 1

    def is_proper(self):
        if not isinstance(self.num, int) or not isinstance(self.den, int):
            raise TypeError("Pas des nombres entiers")
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        if not isinstance(self.num, int) or not isinstance(self.den, int):
            raise TypeError("Pas des nombres entiers")
        return self.num == 1

    def is_adjacent_to(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("pas une fraction")

        diff = abs(float(self) - float(other))
        if diff == 0:
            raise ValueError("Les fractions sont égales")
        return 1/diff == round(1/diff)
