n = 8
matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8

for i in range(n):                    # заполняем главную диагональ единицами, а побочную двойками
    matrix[i][i] = 1
    matrix[i][n-i-1] = 2

for r in range(n):                    # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()