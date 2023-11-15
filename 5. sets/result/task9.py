x1 = {i for i in input().split()}
x2 = {i for i in input().split()}

print(*sorted(x1 | x2))
