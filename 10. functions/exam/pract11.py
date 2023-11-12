from operator import add, sub, mul, truediv


def arithmetic_operation(operation):
    oper = {"+": add,
            "-": sub,
            "*": mul,
            "/": truediv
            }
    return oper[operation]
