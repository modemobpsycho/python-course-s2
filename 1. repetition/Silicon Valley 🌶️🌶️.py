virus = "anton"
for i in range(1, int(input()) + 1):
    s = input()
    res = ''
    for x in virus:
        if x in s:
            res += x
            s = s[s.find(x):]
    if res == virus:
        print(i, end=' ')
