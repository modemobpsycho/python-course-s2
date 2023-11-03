def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)

    return acc