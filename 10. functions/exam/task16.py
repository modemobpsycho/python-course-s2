from functools import reduce

numbers = [1, 2, 3]
result = reduce(lambda a, b: a * b, numbers, 10)
print(result)
