n = int(input())
symb = set()
for _ in range(n):
    for x in input().lower():
        symb.add(x)
print(len(symb))