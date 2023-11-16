matrix = []
n = int(input())
for i in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)

max_d = matrix[0][0]

for i in range(n):
    for j in range(n):
        if i >= j and matrix[i][j] > max_d:
            max_d = matrix[i][j]
print(max_d)
