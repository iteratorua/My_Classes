"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить
ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

def company_parse_def(file_name):
    try:
        all_margin = 0
        my_dict = {}
        my_whole_list = []
        list_plus_profit = []
        average_profit = 0
        with open(file_name, "r", encoding="utf-8") as f_obj:
            for lines in f_obj.readlines():
              # lines = lines.replace("\ufeff", "")
                my_list = lines[:-1].split(" ")
                my_list.append(int(my_list[2])-int(my_list[3]))
                if my_list[4]>0:
                    all_margin += my_list[4]
                my_whole_list.append(list(my_list))
            average_profit = all_margin/len(my_whole_list)
            for el in my_whole_list:
                my_dict.update({el[0]:el[4]})
            list_plus_profit.append(my_dict)
            list_plus_profit.append({'average_profit':average_profit})
            with open("my_file.json", "w") as write_f:
                json.dump(list_plus_profit, write_f)
    except:

        print("Что-то пошло не так.")


company_parse_def("company_info.txt")
