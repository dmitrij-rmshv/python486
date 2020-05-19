# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div_func(divisible, divider):
    try:
        return divisible / divider
    except ZeroDivisionError:
        return


var_1 = int(input("Введите делимое: "))
var_2 = int(input("Введите делитель: "))
div_result = div_func(var_1, var_2)
print(f"Частное от деления равно : {div_result}") if div_result else print("Нельзя делить на ноль")
