# put your python code here
s = [tuple(input().split()) for i in range(int(input()))]

for i in s:
    print(*i)
print()

for i in s:
    if int(i[1]) >= 4:
        print(*i)
