def greet(name, *args):
    s = " and ".join((name, ) + args)
    return f"Hello, {s}!"