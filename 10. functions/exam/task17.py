from functools import reduce

words = ['beegeek', 'stepik', 'python', 'iq-option']
result = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(result)
