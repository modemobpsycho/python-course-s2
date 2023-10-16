x = input().split()
n, m = int(x[0]), int(x[1])
matrix = []

tmp = [i for i in range(1, m + 1)]
matrix = []
    
for i in range(n):
    matrix.append(tmp)
    tmp = tmp[1:] + [tmp[0]]
            
for i in range(n):
    print(*matrix[i])
