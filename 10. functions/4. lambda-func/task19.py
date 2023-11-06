from functools import reduce


def evaluate(coeff, x): return reduce(lambda s, a: s * x + a, coeff)


print(evaluate(map(int, input().split()), int(input())))
