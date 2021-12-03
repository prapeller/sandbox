import re


class ComplexNumber:
    def __init__(self, z_string):
        regex_a = re.compile(r'\W*\d\.*\d*')
        regex_b = re.compile(r'\W*\d*\.*\d*i')

        match_a = re.search(regex_a, z_string)
        match_b = re.search(regex_b, z_string)

        self.a = float(match_a.group())
        try:
            self.b = float(match_b.group()[:-1].replace(' ', ''))
        except ValueError:
            self.b = 1.0 if match_b.group()[:-1].replace(' ', '') == '+' else -1.0

    def __str__(self):
        a = int(self.a) if self.a % 1 == 0 else float(self.a)
        b = int(self.b) if self.b % 1 == 0 else float(self.b)
        sign = '+' if b > 0 else ''
        if b == 1 or b == -1:
            return f'{a} {sign}i'
        else:
            return f'{a} {sign}{b}i'

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        sign = '+' if b > 0 else ''
        return ComplexNumber(f'{a} {sign}{b}i')

    def __mul__(self, other):
        a = self.a * other.a - (self.b * other.b)
        b = self.a * other.b + self.b * other.a
        sign = '+' if b > 0 else ''
        return ComplexNumber(f'{a} {sign}{b}i')


z_1 = ComplexNumber('1.25-3i')
z_2 = ComplexNumber('3+i')
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
