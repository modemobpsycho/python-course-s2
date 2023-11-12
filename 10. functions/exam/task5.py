def outer_func(a, b):
    def inner_func(c, d):
        return c + d + a*b
    return inner_func


res = outer_func(5, 10)(3, 2)

print(res)
