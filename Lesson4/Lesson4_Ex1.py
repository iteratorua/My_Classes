from sys import argv

def salary(argv):
    try:
        return float(argv[1])*float(argv[2])+float(argv[3])
    except BaseException:
        print("Ошибка в аргументах. Должны быть 3 числа.")

print(salary(argv))