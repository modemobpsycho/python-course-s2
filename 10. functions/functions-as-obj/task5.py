import math


def pwr(p):

    def n_power(n):
        return n**p

    return n_power


commands = {
    "квадрат": pwr(2),
    "куб": pwr(3),
    "корень": pwr(0.5),
    "модуль": abs,
    "синус": math.sin
}

n = int(input())
command = input()

print(commands[command](n))