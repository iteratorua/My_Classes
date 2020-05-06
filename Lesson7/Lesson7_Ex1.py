"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

"""
class Matrix(list):
    mtxlst = []
    def __init__(self, intro_lst):
        self.mtxlst = intro_lst
    def __str__(self):
        return_str = ""
        for el in self.mtxlst:
            i = 0
            while i<len(el):
                return_str+=(str(el[i]) + "    ")
                if i==len(el)-1:
                    return_str+="\n"
                i+=1
        return return_str
    def __add__(self, other):
       res_lst = self.mtxlst
       for i in range(len(self.mtxlst)):
            for j in range(len(self.mtxlst[0])):
                res_lst[i][j] = res_lst[i][j]+ other.mtxlst[i][j]
       return Matrix(res_lst)

lst1 = [[32,22],[37,43],[51,82]]
lst2 = [[32,5,32],[2,4,6],[-1,64,-8]]
lst3 = [[33,55],[17,36],[22,33]]
my_element1= Matrix(lst1)
my_element2 = Matrix(lst2)
my_element3 = Matrix(lst3)
print(str(my_element1))
print(str(my_element3))
print(str(my_element1 + my_element3))
