a, b = int(input()), int(input())

for i in range(a, b + 1):
    digits = [int(q) for q in str(i)]
    if all(map(lambda x: x != 0 and i % x == 0, digits)):  # type: ignore
        print(i, end=' ')
