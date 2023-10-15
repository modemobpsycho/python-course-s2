x = input().split()
n, m = int(x[0]), int(x[1])
matrix = []
for _ in range(n):
    tmp = [i for i in range(m)]
    matrix.append(tmp)

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            matrix[i][j] = "."
        else:
            matrix[i][j] = "*"

for i in range(n):
    print(*matrix[i])
