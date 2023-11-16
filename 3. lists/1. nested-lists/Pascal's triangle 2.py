n = int(input())
list = [[1]]
for i in range(1, n):
    row = [1] * (i + 1)
    for q in range(i + 1):
        if q != 0 and q != i:
            row[q] = list[i - 1][q - 1] + list[i - 1][q]
    list.append(row)
for r in list:
    print(*r)