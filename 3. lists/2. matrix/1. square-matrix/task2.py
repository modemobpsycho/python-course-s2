matrix = []
n = int(input())
for i in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)

total = 0
for i in range(n):                    # выводим матрицу
    for j in range(n):
        if i == j:
            total += matrix[i][j]

print(total)
