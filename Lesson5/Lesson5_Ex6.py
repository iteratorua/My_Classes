"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
 содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

def course_def(file_name):
    try:
            my_dict={}
            with open(file_name,"r",encoding="utf-8") as f_obj:
                for lines in f_obj.readlines():
                    lines = lines.replace("\n","")
                    if lines[len(lines)-1]==".":
                        lines = lines[:len(lines)-1]
                    lines = lines.replace("(л)","")
                    lines = lines.replace("(пр)","")
                    lines = lines.replace("(лаб)","")
                    lines = lines.replace("—","0")
                    my_list = lines[:].split(" ")
                    my_dict.update({my_list[0]:(int(my_list[1])+int(my_list[2])+int(my_list[3]))})
            print(my_dict)
    except:
            print("Что-то пошло не так.")


course_def("course.txt")
