# put your python code here
x1 = set(int(i) for i in input().split())
x2 = set(int(i) for i in input().split())
x3 = set(int(i) for i in input().split())

print(*sorted((x1 | x2 | x3) - (x1 & x2 & x3)))

