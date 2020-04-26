my_list = [9, 6, 7,4, 5,3, 2]

N = len(my_list)
i=0
while i < N-1:
    j = 0
    while j<(N-1-i):
        if my_list[j] < my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        j+=1
    i += 1
digit = int(input("Введите число из заданного массива "+str(my_list)+": "))
i = 0
if digit < my_list[len(my_list)-1]:
    my_list.insert(len(my_list),digit)
else:
    for every in my_list:
        if digit > every:
            my_list.insert(i, digit)
            break
        i += 1
print(my_list)