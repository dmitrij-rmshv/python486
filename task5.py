"""
Реализовать структуру «Рейтинг», представляющую собой невозрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
 то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [7, 5, 3, 3, 2]
while True:  # Ввод нового элемента с проверкой адекватности
    new_el = input('Введите новый элемент в рейтинг (целое число) - ')
    if new_el.isdigit():
        new_el = int(new_el)
        break
inserted = False  # Переменная для проверки включения элемента в список
for ind, el in enumerate(my_list):  # Перебор элементов слева направо и вставка в нужную позицию
    if new_el > el:
        my_list.insert(ind, new_el)
        inserted = True
        break
if not inserted:  # Если не вставлен, значит элемент наименьший - вставляем в конец
    my_list.append(new_el)
print(my_list)
