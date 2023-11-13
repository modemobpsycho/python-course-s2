file = open("lines.txt", encoding="utf-8")

print(set(file.readlines()).pop())

file.close()
