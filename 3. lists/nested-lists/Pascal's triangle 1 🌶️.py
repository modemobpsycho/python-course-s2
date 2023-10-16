n = int(input())
lst = [[1]]
for i in range(1, n + 1):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
    lst.append(row)
            
print(lst[-1])