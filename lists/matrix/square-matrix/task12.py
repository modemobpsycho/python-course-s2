n = int(input())
matrix = []
flag = True
for _ in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)
    
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i] and i != j:
            flag = False
            break
if flag:
    print("YES")
else:
    print("NO")