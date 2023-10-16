x = input().split()
n, m = int(x[0]), int(x[1])
matrix = []
for _ in range(n):
    tmp = [i for i in range(m)]
    matrix.append(tmp)
    
count = 1    
for i in range(n):
    for j in range(m):
        matrix[i][j] = count
        count += 1

for i in range(n):
    if i % 2 != 0:
        matrix[i].reverse()

for i in range(n):
    print(*matrix[i])