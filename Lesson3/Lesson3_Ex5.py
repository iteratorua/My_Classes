def sum_ma():
    sum = 0
    while True:
        new_str = input("Введите числа разделенные пробелом или наберите выход:")
        my_list = new_str.split()
        for every in my_list:
            if every == "выход":
                print(sum)
                return
            sum += float(every)
        print(sum)
sum_ma()
