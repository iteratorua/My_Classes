import random
my_list = [int(el*random.random()*10) for el in range(1,10) ]
my_result_list = [el for el in my_list if (((my_list.index(el)+1)%2==0) and ( my_list[my_list.index(el)]>my_list[my_list.index(el)-1]) )]
print(my_list)
print(my_result_list)