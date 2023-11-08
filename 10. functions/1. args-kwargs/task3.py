def mean(*args):
    s = [i for i in args if type(i) in (int, float)]
    if len(s) == 0:
        return 0.0
    return sum(s) / len(s)
