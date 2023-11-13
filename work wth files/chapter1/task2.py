file = open("numbers.txt", encoding="utf-8")

print(sum(map(int, file)))

file.close()
