# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#  и возвращает сумму наибольших двух аргументов.


def my_func(var_1, var_2, var_3):
    arg_list = [var_3 + var_1, var_1 + var_2, var_2 + var_3]
    return max(arg_list)


num_1 = int(input("Введите первое число : "))
num_2 = int(input("Введите второе число : "))
num_3 = int(input("Введите третье число : "))
print(f"Сумма двух наибольших чисел: {my_func(num_1, num_2, num_3)}")
