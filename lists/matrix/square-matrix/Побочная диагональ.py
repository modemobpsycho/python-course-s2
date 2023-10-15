n = int(input())
matrix = []
for _ in range(n):
    tmp = [int(i) for i in range(n)]
    matrix.append(tmp)
    
for i in range(n):
    for j in range(n):
        if i == n - 1 - j:
            matrix[i][j] = 1
        elif i < n - 1 - j:
            matrix[i][j] = 0
        elif i > n - 1 - j:
            matrix[i][j] = 2
            
for i in range(n): 
    print(*matrix[i])