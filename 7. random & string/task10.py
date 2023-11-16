# put your python code here
import random

numbers = random.sample(list(range(1, 76)), 25)

matrix = [numbers[i:i + 5] for i in range(0, 21, 5)]
matrix[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
