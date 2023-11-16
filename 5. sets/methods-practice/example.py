myset = set([1, 2, 2, 3, 4, 4, 4])
print(len(myset))

myset = set('ъъ эээ юююю яяяяя')
print(len(myset))

myset1 = set([1, 2, 3, 4, 5])
myset2 = set('12345')

print(myset1 == myset2)

numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}

sorted_numbers = sorted(numbers)
print(*sorted_numbers, sep='\n')

myset1 = {1, 2, 3, 3, 3, 3}
myset2 = {2, 1, 3}
myset3 = {1, 2, 3, 4}

print(myset1 == myset2)
print(myset1 == myset3)
print(myset1 != myset3)

numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}

sortnumbers = sorted(numbers, reverse=True)
print(*sortnumbers, sep='\n')
