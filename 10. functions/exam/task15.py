from functools import reduce

numbers = [1, 2, 3]
result = reduce(lambda x, y: x + y, numbers)
print(result)
