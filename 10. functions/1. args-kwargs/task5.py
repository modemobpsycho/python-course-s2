def print_products(*args):
    x = [i for i in args if type(i) == str and len(i) > 1]
    if len(x) == 0:
        print("Нет продуктов")
    else:
        for i in range(1, len(x) + 1):
            print(f"{i}) {x[i - 1]}")