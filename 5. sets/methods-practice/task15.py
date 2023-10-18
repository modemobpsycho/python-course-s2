# put your python code here
x1, x2 = set(input()), set(input())

if x1.isdisjoint(x2):
    print("NO")
else:
    print("YES")
