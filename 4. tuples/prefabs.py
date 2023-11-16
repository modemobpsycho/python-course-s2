# если нужны индексы элементов
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in range(len(numbers)):
    print(numbers[i])

# если индексы не нужны
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for num in numbers:
    print(num)

# распаковка кортежа
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
languages = ('Python', 'C++', 'Java')

print(*numbers)
print(*languages, sep='\n')

# сравнение кортежей
print((1, 8) == (1, 8))  # true
print((1, 8) != (1, 10))  # true
print((1, 9) < (1, 2))  # false
print((2, 5) < (6,))  # true
print(('a', 'bc') > ('a', 'de'))  # false

# сортировка кортежей
not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
print(not_sorted_tuple)

# без изменения исходника и без преобразований
sorted_tuple = tuple(sorted(not_sorted_tuple))
print(sorted_tuple)
#
not_sorted_tuple = ('cc', 'aa', 'dd', 'bb')
tmp = list(not_sorted_tuple)  # через преобразование в список
tmp.sort()

sorted_tuple = tuple(tmp)
print(sorted_tuple)
