def display(*args):
    for i in args:
        print(i, end=' ')


display(name='Emma', age=25) # type: ignore
