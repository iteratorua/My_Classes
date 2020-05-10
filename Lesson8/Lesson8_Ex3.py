"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у
пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных
элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
 сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
 При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента
 и вносить его в список, только если введено число. Класс-исключение должен не позволить
 пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом
 работа скрипта не должна завершаться.

"""

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False
my_list = []
while True:
    digit1 = input("Введите новый числовой элемент списка: ")
    if digit1 =="stop":
        break
    try:
            if is_digit(digit1)==True:
                my_list.append(digit1)
            else:
                raise OwnError("Вводить можно только числа")
    except OwnError as err:
        print(err)

print("Ваш список: "+str(my_list))