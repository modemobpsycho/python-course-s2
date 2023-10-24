s1 = sorted([i for i in input().lower() if i.isalpha()])
s2 = sorted([i for i in input().lower() if i.isalpha()])
if s1 == s2:
    print("YES")
else:
    print("NO")
