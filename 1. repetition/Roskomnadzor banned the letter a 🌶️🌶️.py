word = input() + ' запретил букву'
alph = [chr(i) for i in range(1072, 1104) if chr(i) != 'ё']
for x in alph:
    if x in word:
        print(word, x)
        word = word.replace(x, '').replace('  ', ' ').strip()