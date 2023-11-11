options = ["камень", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

print(res)
