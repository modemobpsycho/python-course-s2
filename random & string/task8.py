import random

my_set = set()

while len(my_set) != 100:
    my_set.add(random.randint(1000000, 9999999))

print(*my_set, sep='\n')
