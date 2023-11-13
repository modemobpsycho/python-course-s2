file = open("nums.txt", encoding="utf-8")

print(sum(map(int, file.read().split())))

file.close()
