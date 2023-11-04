def func(number):
    if (number % 19 == 0 or number % 13 == 0):
        return True
    else:
        return False
    
    
print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))