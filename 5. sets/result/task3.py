# put your python code here
s = [input() for _ in range(int(input()) + 1)]
if len(s) == len(set(s)):
    print("OK")
else:
    print("REPEAT")