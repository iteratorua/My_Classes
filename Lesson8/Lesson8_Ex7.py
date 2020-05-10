"""

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение
 и умножение созданных экземпляров. Проверьте корректность полученного результата.

"""

class Complex_Digit():
    def __init__(self,flt_part,mir_part):
        self.flt_part = flt_part
        self.mir_part = mir_part
    def print_digit(self):
        print("Ваше комплексное число z={}+{}*i".format(self.flt_part,self.mir_part))
    def __add__(self, other):
        return Complex_Digit(self.flt_part+other.flt_part,self.mir_part+other.mir_part)
    def __mul__(self, other):
        #a+bi и c+di:
        #(ac-bd)+(bc+ad)i
        return Complex_Digit(self.flt_part*other.flt_part-self.mir_part*other.mir_part,self.mir_part*other.flt_part+self.flt_part*other.mir_part)

one = Complex_Digit(2,3)
one.print_digit()
two = Complex_Digit(4,5)
(one + two).print_digit()
(one*two).print_digit()