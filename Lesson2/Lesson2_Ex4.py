my_str = input("Введите строку, разделенную пробелами: ")
my_list = my_str.split(" ")
i = 1
for every in my_list:
    print(str(i) + ": " + every[:10] )
    i += 1