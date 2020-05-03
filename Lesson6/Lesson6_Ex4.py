"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните
доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

"""

class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False
    def go(self):
        print("Car say go")
    def stop(self):
        print("Car say stop")
    def turn(self,direction):
        print("Car turn " + direction)
    def showSpeed(self):
        print("Current speed is " + str(self.speed))
    def __init__(self, fspeed, fcolor, fname, fis_police):
        self.speed = fspeed
        self.color = fcolor
        self.name = fname
        self.is_police = fis_police


class TownCar(Car):
    def showSpeed(self):
        print("Towncar speed is {} {} and is police? - {}: ".format(self.color,self.name,self.is_police) + str(self.speed))
        if self.speed>60:
            print("Speed is higher than limit 60")

class WorkCar(Car):
    def showSpeed(self):
        print("Workcar speed is {} {} and is police? - {}: ".format(self.color,self.name,self.is_police) + str(self.speed))
        if self.speed>40:
            print("Speed is higher than limit 40")


twn_car = TownCar(100,"blue","Bentley",False)
twn_car.showSpeed()
wrk_car = WorkCar(60, "red", "Renault", True)
wrk_car.showSpeed()