"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
 на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
 и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую
 структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать
строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум
возможностей, изученных на уроках по ООП.

"""

class Warehouse():
    __division_list_dict = {}
    __division_stock_dict = {}
    __warehouse_stock_list ={}
    def __init__(self, square, shelfqty):
        self.__square = square
        self.__shelfqty = shelfqty
    def add_division(self, division_id, division_name):
        self.__division_list_dict[division_id]=division_name
    def receive_item(self, product_id):
        if product_id in self.__warehouse_stock_list:
            self.__warehouse_stock_list[product_id]+=1
        else:
            self.__warehouse_stock_list[product_id]=1
    def send_item(self, division_id, product_id):
        if division_id in self.__division_stock_dict:
            self.__division_stock_dict[division_id].append(product_id)
        else:
            self.__division_stock_dict[division_id]=[]
            self.__division_stock_dict[division_id].append(product_id)

    def division_info(self,division_id):
        print("В этом отделе: " + str(self.__division_stock_dict[division_id]))
    def warehose_general_info(self):
        print("Площадь склада:" + str(self.__square))
        print("Количество полок: " + str(self.__shelfqty))
    def division_list(self):
        print("Отделы " + str(self.__division_list_dict))
    def stock_list(self):
        print("Запасы "+ str(self.__warehouse_stock_list))


class Device():
    def __init__(self, id,brand, model, price):
        self.__id = id
        self.__brand = brand
        self.__model = model
        self.__price = price
    def get_info(self):
        print("Brand = " + self.__brand, " Model = " + self.__model)

class Printer(Device):
    def __init__(self,id,brand, model, price,speed, paperqty):
        super().__init__(id,brand,model,price)
        self.speed = speed
        self.paperqty = paperqty
    def printing(self, text):
        print("Поставлена задача печати текста: " + text)
class Scanner(Device):
    def __init__(self,id,brand, model, price,speed, resolution):
        super().__init__(id,brand,model,price)
        self.speed = speed
        self.resolution = resolution
    def scanning(self, txt):
        print("Поставлена задача печати текста: " + text)
class Copier(Device):
    def __init__(self, id,brand,model,price,copy_speed):
        super().__init__(id,brand,model,price)
        self.copy_speed = copy_speed
    def coping(self, txt):
        print("Поставлена задача копирования текста: " + text)

first_printer = Printer(17,"Oki","220",20,200,300)
first_scanner = Scanner(18,"Xerox","2230",30,300,200)
first_copier = Copier(20,"Lenovo","222",50,2000)
first_printer.get_info()
first_scanner.get_info()
first_copier.get_info()
my_warehouse = Warehouse(300,400)
my_warehouse.warehose_general_info()
my_warehouse.add_division(1,"Первый")
my_warehouse.add_division(2,"Второй")
my_warehouse.division_list()
my_warehouse.receive_item(17)
my_warehouse.receive_item(17)
my_warehouse.receive_item(17)
my_warehouse.receive_item(18)
my_warehouse.receive_item(20)
my_warehouse.receive_item(20)
my_warehouse.receive_item(17)
my_warehouse.receive_item(20)
my_warehouse.receive_item(18)
my_warehouse.stock_list()
my_warehouse.send_item(1,17)
my_warehouse.send_item(1,17)
my_warehouse.send_item(1,18)
my_warehouse.division_info(1)