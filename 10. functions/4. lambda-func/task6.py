numbers = [1, 2, 5, 3, 4]
numbers.sort(key=lambda x: -x)
print(numbers)


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
result = list(filter(lambda: True, primes))
print(result)


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
result = list(filter(lambda x: True, primes))
print(result)


full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('ben', 'affleck'))