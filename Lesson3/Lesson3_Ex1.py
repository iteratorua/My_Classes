def division(arg1, arg2):
    if arg2 ==0:
        print("Делить на ноль нельзя")
        return
    return arg1/arg2

digit1 = float (input( "Введите делимое число: " ) )
digit2 = float (input( "Введите введите делитель: " ))
print("Результат деления: " + str(division(digit1,digit2))[:7])