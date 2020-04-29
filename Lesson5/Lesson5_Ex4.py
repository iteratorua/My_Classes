"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""


def replace_def(file_name):
    try:
        dict_words = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
        with open(file_name, encoding="utf-8") as f_obj:
            with open("result_digits.txt","w",encoding="utf-8") as f1_obj:
                first = False
                for lines in f_obj.readlines():
                    if first == False:
                        temp_list = lines[1:].split(" ")
                        first = True
                    else:
                        temp_list = lines.split(" ")
                    temp_list[0] = dict_words.get(temp_list[0])
                    f1_obj.writelines(" ".join(temp_list))
    except:
        print("Что-то пошло не так.")


replace_def("digits_list.txt")
