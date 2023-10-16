n = int(input())
matrix = []
for _ in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)
    
for i in range(n):
    matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]
          
for i in range(n):
    print(*matrix[i])

