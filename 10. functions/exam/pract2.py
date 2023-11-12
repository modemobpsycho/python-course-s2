def pretty_print(data, side='-', delimiter='|'):
    stroka = f' {delimiter} '.join(map(str, data))
    print('', (len(stroka) + 2) * side)
    print(delimiter, stroka, delimiter)
    print('', (len(stroka) + 2) * side)
