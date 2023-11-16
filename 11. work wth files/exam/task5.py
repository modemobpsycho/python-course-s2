with open(input(), encoding="utf-8") as words_file, open("forbidden_words.txt", encoding="utf-8") as forbidden_file:
    forbidden_words = forbidden_file.read().split()
    for s in words_file:
        for x in forbidden_words:
            while x in s.lower():
                index = s.lower().index(x)
                s = s[:index] + '*' * len(x) + s[index+len(x):]
        print(s.strip())
