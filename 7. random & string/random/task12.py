import string
import random


def generate_password(length):
    symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits[
        2:]
    symbols = ''.join([symbol for symbol in symbols if symbol not in "IloO"])
    return ''.join(random.sample(symbols, length))


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')