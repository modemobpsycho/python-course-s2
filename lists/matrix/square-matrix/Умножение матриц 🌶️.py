n, m = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for j in range(n)]
input()
n2, m2 = [int(i) for i in input().split()]
matrix2 = [[int(i) for i in input().split()] for j in range(n2)]
matrix3 = [[0] * m2 for _ in range(n)]

for i in range(n):
    for j in range(m2): 
          for k in range(m):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

for i in range(n):
    print(*matrix3[i])
