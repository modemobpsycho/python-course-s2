import random

my_set = set()

while True:
    my_set.add(random.randint(1, 49))
    if (len(my_set)) == 7:
        break
        
print(*sorted(my_set))