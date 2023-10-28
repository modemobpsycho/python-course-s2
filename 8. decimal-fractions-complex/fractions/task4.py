# put your python code here
from fractions import Fraction

a, b = input(), input()

print(f"{a} + {b} = {Fraction(a) + Fraction(b)}")
print(f"{a} - {b} = {Fraction(a) - Fraction(b)}")
print(f"{a} * {b} = {Fraction(a) * Fraction(b)}")
print(f"{a} / {b} = {Fraction(a) / Fraction(b)}")
