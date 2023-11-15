import random

with open("first_names.txt", encoding="utf-8") as names, open("last_names.txt", encoding="utf-8") as lastnames:
    last_names = lastnames.readlines()
    first_names = names.readlines()

for i in range(3):
    print(f"{random.choice(first_names).strip()} {random.choice(last_names).strip()}")
