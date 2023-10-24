# put your python code here
my_dict = {}

for _ in range(int(input())):
    country, *cities = input().split()
    my_dict[country] = cities
    
for _ in range(int(input())):
    city = input()
    for country, cities in my_dict.items():
        if city in cities:
            print(country)
