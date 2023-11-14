with open("file.txt", encoding = "utf-8") as file:
    text = file.read()
    len_count = len(list(filter(lambda x: x.isalpha(), text)))
    words_count  = len(text.split())
    lines_count = len(text.splitlines())
    
print(f"Input file contains:\n{len_count} letters\n{words_count} words\n {lines_count} lines")