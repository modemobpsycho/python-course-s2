with open("grades.txt", encoding="utf-8") as file:
    counter = 0
    for line in file:
        counter += all(map(lambda x: int(x) >= 65, line.split()[1:]))
    print(counter)
