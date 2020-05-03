"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""

class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage":0, "bonus":0}
    def __init__(self, fname, fsurname, fposition):
        self.name = fname
        self.surname = fsurname
        self.position = fposition
    def set_income(self, fwage, fbonus):
        self._income["wage"] = fwage
        self._income["bonus"] = fbonus
    def get_income(self):
        return self._income

class Position(Worker):
    def get_full_name(self):
        print("Сотрудника зовут " + self.name+ " " + self.surname)
    def get_total_income(self):
        print("Оклад составляет " + str(self.get_income()["wage"]+self.get_income()["bonus"])+" долЯров")

new_worker = Position("Misha","Pazynych","General Manager")
new_worker.set_income(1000,2000)
new_worker.get_full_name()
new_worker.get_total_income()