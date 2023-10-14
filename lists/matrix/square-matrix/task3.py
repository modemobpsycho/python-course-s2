matrix = []
n = int(input())
for i in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)

for i in range(n):
    total = 0
    count = 0
    for j in range(n):
        total += matrix[i][j]
    for k in range(n):
        if matrix[i][k] > total / n:
            count += 1
    print(count)
