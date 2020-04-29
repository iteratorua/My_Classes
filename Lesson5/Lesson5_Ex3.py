"""
Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников
имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
def employee_salary(file_name):
    try:
        with open(file_name) as f_obj:
            for lines in f_obj.readlines():
                temp_list = lines[:-1].split(" ")
                if float(temp_list[1])>=20000:
                   print("Сотрудник {} получает зарплату {}".format(temp_list[0],temp_list[1]))
    except:
        print("Что-то пошло не так.")

employee_salary("salary_list.txt")