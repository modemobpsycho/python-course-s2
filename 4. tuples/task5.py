poet_data = ('Пушкин', 1799, 'Санкт-Петербург')

poet_data = list(poet_data)
poet_data[-1] = "Москва"
poet_data = tuple(poet_data)
print(poet_data)