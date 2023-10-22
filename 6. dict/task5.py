s = input().upper()
keyboard = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
for symbol in s:
    for key, value in keyboard.items():
        if symbol in value:
            print(key * (value.index(symbol) + 1), end='')