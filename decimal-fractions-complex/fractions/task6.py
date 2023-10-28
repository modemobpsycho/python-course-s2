from fractions import Fraction
import math

n = int(input())

print(sum([Fraction(1, math.factorial(i)) for i in range(1, n + 1)]))
