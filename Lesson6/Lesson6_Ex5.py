"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы
должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.

"""
class Stationery:
    title = ""
    def draw(self):
        print("Запуск отисовки")
    def __init__(self, ftitle):
        self.title = ftitle

#Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).

class Pen(Stationery):
    def draw(self):
        print("You are inside Pen:)" + self.title)

class Pencil(Stationery):
    def draw(self):
        print("You are inside Pencil:) " + self.title)

class Handle(Stationery):
    def draw(self):
        print("You are inside Handle:) " + self.title)

fPen = Pen("Happy Pen")
fPencil = Pencil("Happy Pencil")
fHandle = Handle("Happy Handle")
fPen.draw()
fPencil.draw()
fHandle.draw()

