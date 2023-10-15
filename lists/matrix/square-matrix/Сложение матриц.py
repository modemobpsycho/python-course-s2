x = input().split()
n, m = int(x[0]), int(x[1])
matrix1 = [[int(x) for x in input().split()] for _ in range(n)]
pustaya_stroka = input()
matrix2 = [[int(x) for x in input().split()] for _ in range(n)]
matrix3 = [[int(x) for x in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):       
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

for i in range(n):
    print(*matrix3[i])




