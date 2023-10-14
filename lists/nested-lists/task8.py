n = int(input())
my_list = []

for i in range(1, n + 1):
    my_list.append([int(q) for q in range(1, i + 1)])
print(*my_list, sep = '\n')