desc_list = []
dict_car = {}
tuple_list =[]
list_values =[]
total_dict = {}
while True:
    new_element = input("Введите новую характеристику позиции или введите выход: ")
    if new_element == "выход":
        break
    desc_list.append(new_element)

i = 0
if len(desc_list) > 0:
    while True:
        temp_tuple = ()
        if input("Если хотите закончить ввод введите н, продолжить нажмите Enter:") == "н":
            break;
        for every in desc_list:
            dict_car.update({every: input("Введите " + every + ": ")})
        temp_tuple = (i+1, dict(dict_car))
        tuple_list.append(tuple(temp_tuple))
        i += 1
for every in desc_list:
    list_values.clear()
    for elem in tuple_list:
        list_values.append(elem[1].get(every))
    total_dict[every] = list(list_values)
print(tuple_list)
print(total_dict)