total = 0
my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]

for li in my_list:
    total += len(li)

print(total)



list1 = [1, 7, 12, 0, 9, 100] 
list2 = [1, 7, 90] 
list3 = [1, 10]

print(min(list1, list2, list3))
print(max(list1, list2, list3))



list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]

print(min(list1))
print(max(list1))
print(min(list2))
print(max(list2))