n = int(input())
matrix = []
for _ in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)
    
for i in range(n):
    for j in range(n - 1, -1, -1):
        print(matrix[j][i], end=' ')
    print()