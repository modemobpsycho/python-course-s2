from random import choice, randint
import string


def generate_index():
    up_letter = string.ascii_uppercase
    s1, s2, s3, s4 = (choice(up_letter) for _ in range(4))
    num1, num2 = (randint(0, 99) for _ in range(2))
    return f"{s1}{s2}{num1}_{num2}{s3}{s4}"
