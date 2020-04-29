'''
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
'''


def file_calculation(file_name):
    lines_qty=0
    sum = []
    with open(file_name) as f_obj:
        print(f_obj.buffer)
        for line in f_obj:
            my_list_len = len(line.split())
            sum.append(len(line.split()))
            lines_qty +=1
    return lines_qty,sum

a,b = file_calculation("count_smth.txt")
print("Количество строк {}, количество слов в каждой строке {}".format(a,b))
