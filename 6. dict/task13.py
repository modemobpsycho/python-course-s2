my_dict = {}

for _ in range(int(input())):
    key, value = input().split(': ')
    my_dict[key.lower()] = value
               
for _ in range(int(input())):
    key = input().lower()
    print(my_dict.get(key, "Не найдено"))