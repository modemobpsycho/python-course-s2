with open("numbers.txt", encoding="utf-8") as file:
    for line in file:
        print(sum([int(num) for num in line.split()]))
