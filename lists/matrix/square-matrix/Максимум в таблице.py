n, m = int(input()), int(input())
matrix = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)
x, y = 0, 0
matrix_max = matrix[0][0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] > matrix_max:
            matrix_max = matrix[i][j]
            x = i
            y = j

print(x, y)
