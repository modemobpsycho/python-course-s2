s1 = set(int(i) for i in input().split())
s2 = set(int(i) for i in input().split())

print(*sorted(s1 & s2))