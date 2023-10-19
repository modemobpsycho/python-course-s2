x1 = {int(i) for i in input().split()}
x2 = {int(i) for i in input().split()}

if x1.isdisjoint(x2):
    print("BAD DAY")
else:
    print(*sorted(x1 & x2, reverse = True))

