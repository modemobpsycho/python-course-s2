numbers = [int(i) for i in input().split()]
my_set = set()

for i in range(len(numbers)):
    if numbers[i] in my_set:
        print("YES")
    else:
        print("NO")
        my_set.add(numbers[i])