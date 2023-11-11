def chuncked(s, n):
    result = []
    for i in range(0, len(s), n):
        result.append(s[i:i + n])
    return result


s = input().split()
n = int(input())
print(chuncked(s, n))
