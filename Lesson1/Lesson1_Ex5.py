income = float(input("Введите выручку компании: "))
expenses = float(input("Введите расходы компании: "))
if income > expenses:
    print("Ваша прибыль составляет: " + str(income - expenses))
    print("В процентном выражении: " + str((income - expenses) / income))
else:
    print("Ваш убытко составляет: " + str(expenses-income))
personal_qty = int(input("Введите количество персонала: "))
if income > expenses:
    print("Прибыль из расчета на одного сотрудника оставляет " + str((income-expenses)/personal_qty))
