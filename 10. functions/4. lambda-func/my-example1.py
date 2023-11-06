numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]

positive_numbers = list(filter(lambda x: x > 0, numbers)
                        )  # положительные числа
large_numbers = list(filter(lambda x: x > 50, numbers))  # числа, большие 50
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # четные числа

print(positive_numbers)
print(large_numbers)
print(even_numbers)
