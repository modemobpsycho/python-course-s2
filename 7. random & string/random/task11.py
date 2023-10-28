# put your python code here
import random

my_list = [input() for _ in range(int(input()))]

random.shuffle(my_list)

for i in range(len(my_list)):
    print(f"{my_list[i - 1]} - {my_list[i]}")