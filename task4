"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
n = input("Введите целое положительное число: ")
redo_num = int(n)  # клон введенного числа для расчленения в цикле
max_digit = 0

while redo_num > 0:
    digit = redo_num % 10
    if digit == 9:
        max_digit = 9
        break
    elif digit > max_digit:
        max_digit = digit
    redo_num //= 10

print(f"Самая большая цифра в числе {n}: {max_digit}")