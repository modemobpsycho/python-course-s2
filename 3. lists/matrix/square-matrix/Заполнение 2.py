x = input().split()
n, m = int(x[0]), int(x[1])
matrix = []
for _ in range(n):
    tmp = [i for i in range(m)]
    matrix.append(tmp)

count = 1
for j in range(m):
    for i in range(n):
        matrix[i][j] = count
        count += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()
