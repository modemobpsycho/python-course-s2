import random

length = int(input())  # длина пароля
s = ''
for _ in range(length):
    if random.randint(0, 1) == 1:
        s += chr(random.randint(65, 90))
    else:
        s += chr(random.randint(97, 122))
print(s)