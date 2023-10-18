s = input().split()
answer = "YES"
for i in range(1, len(s)):
    if set(s[i - 1]) != set(s[i]):
        answer = "NO"
        break
print(answer)
