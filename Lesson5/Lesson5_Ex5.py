
"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random
def sum_def(file_name):
    try:
        with open(file_name,"w",encoding="utf-8") as f_obj:
            my_list = [el*random.randint(1,10) for el in range(1,10)]
            f_obj.write(" ".join(map(str,my_list)))
            print("Сумма чисел в файле {}".format(sum(my_list)))
    except:
        print("Что-то пошло не так.")


sum_def("sum.txt")