from fractions import Fraction

n = int(input())
my_set = set()

for i in range(1, n):
    for j in range(i + 1, n + 1):
        my_set.add(Fraction(i, j))

print(*sorted(my_set), sep="\n")
