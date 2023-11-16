with open('words.txt', 'w') as output:
    print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
    print('python', file=output)
