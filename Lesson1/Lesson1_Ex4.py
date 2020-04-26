number = int(input("Введите максимальное целое число "))
max_digit = number % 10
number = number // 10
while number > 0:
    if number % 10 > max_digit:
        max_digit = number % 10
    number = number//10
print(max_digit)