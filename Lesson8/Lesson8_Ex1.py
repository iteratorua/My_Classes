"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
@classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

"""


class Date(object):
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def from_string(cls, date_as_string):
       day, month, year = map(int, date_as_string.split('-'))
       return day,month,year

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day not in range (1,32):
            print("Неверный день")
        if month not in range(1,13):
            print("Неверный месяц")
        if year not in range(1,6000):
            print("Неверный год")
        return day <= 31 and month <= 12 and year <= 6000


date2 = Date.from_string('12-11-2020')
print(date2)
is_date = Date.is_date_valid('121-110-2020')
print(is_date)
