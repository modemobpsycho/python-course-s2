def rotate(s):
    return s[::-1]


s = input()

if len(s) == 5:
    print(int(rotate(s)))
else:
    print(int(s[0] + rotate(s[1:])))


#------>>>>>

s = input()
print(int(s[:-5] + s[-5:][::-1]))