km_first_day = float(input("Введите километраж в первый день: "))
km_last_day = float(input("Введите километраж в последний день: "))
temporary = km_first_day
qty_days = 1
while True:
    temporary = temporary*1.1
    qty_days += 1
    if temporary > km_last_day:
        break
print("Дистанция достигнута за " + str(qty_days))



