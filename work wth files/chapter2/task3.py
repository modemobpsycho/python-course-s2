with open("data.txt", encoding="utf-8") as file:
    for line in file.readlines()[::-1]:
        print(line.strip())
