with open("lines.txt", encoding="utf-8") as file:
    text = file.readlines()
    max_len = max(map(len, text))
    print(*filter(lambda x: len(x) == max_len, text), sep='')
