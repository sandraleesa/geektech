class Fraction:
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    def __add__(self, other):
        if type(other) == Fraction:
            a = self.numerator
            b = self.denumerator
            c = other.numerator
            d = other.denumerator
            return Fraction(a * d + b * c, b * d)
        elif type(other) == int:
            return self + Fraction(other)

    def __sub__(self, other):
        if type(other) == Fraction:
            a = self.numerator
            b = self.denumerator
            c = other.numerator
            d = other.denumerator
            return Fraction(a * d - b * c, b * d)
        elif type(other) == int:
            return self + Fraction(other)

    def __mul__(self, other):
        a = self.numerator
        b = self.denumerator
        c = other.numerator
        d = other.denumerator
        return Fraction(a * c, b * d)

    def __floordiv__(self, other):
        if type(other) == Fraction:
            a = self.numerator
            b = self.denumerator
            c = other.numerator
            d = other.denumerator
            return Fraction(a * d, b * c)
        elif type(other) == int:
            return self // Fraction(other)
