# put your python code here
from fractions import Fraction

n = int(input())

print(sum([Fraction(1, i**2) for i in range(1, n + 1)]))
