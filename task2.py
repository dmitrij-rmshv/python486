"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
my_list = list(input('Введите произвольную фразу - '))  # в качестве списка использую строку
print(my_list)
for i in range(len(my_list)):
    if i % 2:  # в пробеге по циклу выбираю нечётные элементы
        my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]  # парный обмен значениями
print(my_list)
