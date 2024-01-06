class Fraction:
    def __init__(self, num=0, den=1):
        """
        This builds a fraction based on some numerator and denominator.

        PRE: den != 0 and num and den are integers
        POST: The fraction is created with the given numerator and denominator
        RAISE: Error if the denominator is 0 or if the numerator or
        denominator are not integers
        """
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
        """
        Return a textual representation of the reduced form of the fraction

        POST: Prints the fraction in the form n/d
        """
        return f"{self.num}/{self.den}"

    def as_mixed_number(self):
        """
        Return a textual representation of the reduced form of the fraction
        as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE: self.num < self.den
        POST: Prints the fraction in the form n/d
        """
        integer_part = self.num // self.den
        remainder = Fraction(self.num % self.den, self.den)
        return f"{integer_part} {remainder}"

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other is a fraction
         POST : Returns the sum of two fractions
        RAISE : TypeError if other is not a fraction
         """
        if not isinstance(other, Fraction):
            raise TypeError("Pas une fraction")
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other is a fraction
        POST : Returns the difference of two fractions
        RAISE : TypeError if other is not a fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Pas une fraction")
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other is a fraction
        POST : Returns the product of two fractions
        RAISE : TypeError if other is not a fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Pas une fraction")
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other is a fraction and other.num != 0
        POST : Returns the quotient of two fractions
        RAISE : ValueError if other.num == 0
        """
        if other.num == 0:
            raise ValueError("Cannot divide by zero")
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __pow__(self, power):
        """Overloading of the ** operator for fractions

        PRE : power is an integer
        POST : Returns the power of a fraction
        RAISE : TypeError if power is not an integer
        """
        if not isinstance(power, int):
            raise TypeError("Pas un entier")
        num = self.num ** power
        den = self.den ** power
        return Fraction(num, den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other is a fraction
        POST : Returns True if the two fractions are equal, False otherwise

        """
        if not isinstance(other, Fraction):
            raise TypeError("Pas une fraction")
        return self.num * other.den == other.num * self.den

    def __float__(self):
        """Returns the decimal value of the fraction

        POST : Returns the decimal value of the fraction
        """
        return self.num / self.den

    def is_zero(self):
        """Check if a fraction's value is 0

        POST : Returns True if the fraction's value is 0, False otherwise
        """
        return self.num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        POST : Returns True if the fraction is integer, False otherwise
        """
        return self.den == 1

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        POST : Returns True if the absolute value of the fraction is < 1,
        False otherwise
        """
        return abs(self.num) < abs(self.den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        POST : Returns True if the fraction's numerator is 1 in its reduced
        form, False otherwise
        """
        return self.num == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference
        them is a unit fraction

        PRE : other is a fraction and self != other
        POST : Returns True if the two fractions are adjacent, False otherwise
        RAISE : ValueError if the two fractions are equal
        """
        if not isinstance(other, Fraction):
            raise TypeError("pas une fraction")
        diff = abs(self.num * other.den - other.num * self.den)
        if diff == 0:
            raise ValueError("Les fractions sont égales")
        return diff == 1
