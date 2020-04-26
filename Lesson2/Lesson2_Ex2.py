my_list =[]
temp_list = []
while True:
    temp = input("Введите элемент списка или введите 'exit' для выхода: ")
    if temp == 'exit':
        break
    my_list.append(temp)
i = 0
while i < (len(my_list)-1):
    temp = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = temp
    i += 2
print(my_list)