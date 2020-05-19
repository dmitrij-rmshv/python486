# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
#  то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def line_summ(line):
    numbers = line.split()
    line_result = 0
    quit_flag = False
    for el in numbers:
        if el.endswith('q'):
            quit_flag = True
            el = el.replace('q', '')
            if el == '':
                break
        try:
            line_result += float(el)
        except ValueError:
            line_result = 0
            print("Ошибка! Повторите ввод.")
            break
    return line_result, quit_flag


print("\n  '''  Программа вычисления суммы чисел  '''  \n")
print("Вводите числа, разделяя пробелом, нажмите Enter\n"
      "При необходимости вводите несколько строк. Для выхода введите 'q'\n")
sum_result = 0
while True:
    line_result, the_end = line_summ(input("-> "))
    if line_result:
        sum_result += line_result
        print(f"Сумма чисел : {sum_result}")
    if the_end:
        break
