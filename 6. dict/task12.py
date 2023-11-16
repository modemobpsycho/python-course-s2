s = input().lower().split()
x = [word.strip(".,!?:;-") for word in s]
my_dict = {}

for i in x:
    my_dict[i] = x.count(i)

result = {}
min_count = min(my_dict.values())

for key, value in my_dict.items():
    if value == min_count:
        result[key] = value

print(min(result))
