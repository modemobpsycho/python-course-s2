with open("population.txt", encoding="utf-8") as file:
    res = [line.split('\t') for line in file]

for i in res:
    if i[0].startswith('G') and int(i[1]) > 500000:
        print(i[0])
