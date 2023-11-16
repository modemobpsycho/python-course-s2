file = open("prices.txt", encoding="utf-8")
total = 0

for line in file:
    product = line.split()
    total += int(product[1]) * int(product[2])

print(total)

file.close()
