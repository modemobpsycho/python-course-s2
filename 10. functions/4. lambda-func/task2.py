users = [('Timur', 28), ('Ruslan', 21), ('Roman', 30),
         ('Soltan', 24), ('Robert', 1)]
result = max(users, key=lambda x: x[1])
print(result)
