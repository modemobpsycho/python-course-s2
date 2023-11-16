with open("nums.txt", encoding="utf-8") as file:
    s = 0
    k = '0'
    for i in file.read():
        if i.isdigit():
            k += i
        else:
            s += int(k)
            k = '0'
    print(s)
