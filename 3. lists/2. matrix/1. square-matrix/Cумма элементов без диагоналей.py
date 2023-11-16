n = int(input())
matrix = []
for k in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            sum1 += matrix[i][j]
        elif i < j and i > n - 1 - j:
            sum2 += matrix[i][j]
        elif i > j and i < n - 1 - j:
            sum3 += matrix[i][j]
        elif i > j and i > n - 1 - j:
            sum4 += matrix[i][j]
print(f"Верхняя четверть: {sum1}")
print(f"Правая четверть: {sum2}")
print(f"Нижняя четверть: {sum4}")
print(f"Левая четверть: {sum3}")
