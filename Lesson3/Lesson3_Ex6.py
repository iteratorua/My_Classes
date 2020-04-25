def int_func(input_string):
    return input_string.title()
input_string = input("Введите строки, разделенные пробелом,и нажмите Enter: ")
my_list = input_string.split()
for i in range(0,len(my_list),1):
    my_list[i]=int_func(my_list[i])
print(' '.join(my_list))