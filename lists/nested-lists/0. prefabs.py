#Create
#method 1
n, m = int(input()), int(input())    #n и m
my_list = []

for _ in range(n):
    my_list.append([0] * m)

print(my_list)

#method 2
n, m = int(input()), int(input())  #n и m
my_list = [0] * n

for i in range(n):
    my_list[i] = [0] * m

print(my_list)

#method 3
n, m = int(input()), int(input())  #n и m, B WAY!!

my_list = [[0] * m for _ in range(n)]

print(my_list)

#read
n = 4                                         # количество строк (элементов)
my_list = []

for _ in range(n):
    elem = [int(i) for i in input().split()]  # создаем список из элементов строки
    my_list.append(elem)
    
#print
#method1
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')  # используем необязательный параметр end
    print()                            # перенос на новую строку
    
#method2 (BETTER!)    
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[j][i], end=' ')  # выводим my_list[j][i] вместо my_list[i][j]
    print()
    
#Find sum
my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]] 

total = 0
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        total += my_list[i][j]

print(total)

my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for row in my_list:
    for elem in row:
        total += elem

print(total)