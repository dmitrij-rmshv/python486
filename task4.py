"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
user_string = input('Введите строку из нескольких слов, разделённых пробелами - ')
string_list = user_string.split()
for ind, el in enumerate(string_list, 1):
    print(ind, el[:10])
