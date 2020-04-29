import random
'''
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

def file_creation():
    try:
        with open(str(random.randint(1,1000))+ "_file.txt","w") as f_obj:
            print("Файл "+ f_obj.name +" создан")
            while True:
                temp_str = input("Введите строку для записи в файл или нажмите Enter для окончания: ")
                if temp_str== "":
                    break
                f_obj.write(temp_str+'\n')
    except:
        print("Что-то пошло не так.")
file_creation()
print("Adios")