s = input()
my_dict = {}

for i in range(int(input())):
    value, key = input().split(": ")
    my_dict[int(key)] = value

for symbol in s:
    print(my_dict[s.count(symbol)], end='')
