n = int(input())
matrix1 = [[int(i) for i in input().split()] for j in range(n)]
matrix2 = matrix1
x = int(input())

for _ in range(x - 1):
    matrix = [[0] * n for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    matrix1 = matrix

for i in range(n):
    print(*matrix1[i])
