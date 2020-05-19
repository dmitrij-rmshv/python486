# 6. Реализовать функцию int_func(),
#  принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
#  но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()


def int_func(word):
    letters_list = list(word)
    for letter in letters_list:
        if ord(letter) < 97 or ord(letter) > 122:
            print("не годится - необходимо вводить ТОЛЬКО маленькие латинские буквы")
            return
    word = word.title()
    return word


def int_func_plus(word):
    word = list(word)
    for letter in word:
        if (not (96 < ord(letter) < 123)) and (not (64 < ord(letter) < 91)) and (not (1039 < ord(letter) < 1104)):
            print("не годится - необходимо вводить ТОЛЬКО буквы")
            return
    first_letter = ord(word[0])
    word[0] = chr(first_letter - 32) if (96 < first_letter < 123) or (1071 < first_letter < 1104) else chr(first_letter)
    return ''.join(word)


while True:
    result_word = int_func(input("Введите слово из маленьких латинских букв : "))
    if result_word:
        print(result_word)
        break

phrase = input("Теперь введите фразу из латинских букв в нижнем регистре : ").split()
for i, el in enumerate(phrase):
    new_word = int_func(el)
    phrase[i] = 'ай-ай' if new_word is None else new_word
print(' '.join(phrase))

phrase = input("Теперь можно ввести фразу из любых букв в любом регистре : ").split()
for i, el in enumerate(phrase):
    new_word = int_func_plus(el)
    phrase[i] = 'ай-ай' if new_word is None else new_word
print(' '.join(phrase))
