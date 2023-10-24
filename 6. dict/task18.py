# put your python code here
my_dict = {}

for _ in range(int(input())):
    value, key = input().lower().split()
    my_dict[key] = my_dict.get(key, []) + [value]

for _ in range(int(input())):
    name = input().lower()
    print(*my_dict.get(name, ["абонент не найден"]))
