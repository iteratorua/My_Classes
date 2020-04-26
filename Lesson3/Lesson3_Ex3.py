def my_func(one, two, three):
    if one<=two and one<=three:
        return two+three
    if two<=one and two<=three:
        return one+three
    if three<=one and three<=two:
        return one+two
print("Сумма наиболших чисел равна: " + str(my_func(3,2,2)))