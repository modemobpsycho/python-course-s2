n = int(input())
digits = [set(input()) for _ in range(n)]
my_set = digits[0]

for i in range(1, len(digits)):
    my_set.intersection_update(digits[i])

print(*sorted(my_set))
