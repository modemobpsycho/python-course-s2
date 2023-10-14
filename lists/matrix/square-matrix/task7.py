inp = input().split()
out = [[]]
for i in range(len(inp)):
    for j in range(len(inp) - i):
        out.append(inp[j:j + i + 1])
print(out)