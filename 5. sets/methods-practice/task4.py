# put your python code here
s1, s2 = input(), input()
s = s1 + s2
if len(set(s)) == 10:
    print("YES")
else:
    print("NO")