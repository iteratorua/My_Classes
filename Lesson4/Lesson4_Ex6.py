from itertools import count, cycle
'''
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''
c=0
for el in count(int(input("Введите первое число счетчика: "))):
    print(el)
    c+=1
    if c>100:
        break
c=0
for el in cycle(["1","2","3"]):
    print(el)
    c+=1
    if c>100:
        break