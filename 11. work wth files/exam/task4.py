with open("words.txt", encoding="utf-8") as file:
    s = file.read().split()
    print(*[i for i in s if len(i) == len(max(s, key=len))], sep='\n')
