def my_func_1(x,y):
    return x**y
def my_func_2(x,y):
    sum = 1
    i=0
    while i<abs(y):
        sum = sum*(1/x)
        i+=1
    return sum
print(my_func_1(2,-4))
print(my_func_2(2,-4))
