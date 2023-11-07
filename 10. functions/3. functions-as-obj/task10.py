def f1(x):
    return 2*x+1


def f2(x):
    return x**2


def f3(x):
    return -x**2+1


def f4(x):
    return x-3


funcs = [f1, f2, f3, f4]
i = int(input())
print(funcs[i](2))