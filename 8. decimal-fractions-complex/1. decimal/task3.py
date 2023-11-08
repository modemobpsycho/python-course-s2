from decimal import Decimal
from math import exp, log10, sqrt

num = Decimal(input())
print(num.exp() + num.ln() + num.log10() + num.sqrt())
