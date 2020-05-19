# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#  имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def user_func(**kwargs):
    """Осуществляет вывод данных о пользователе."""
    print(f"Пользователь {kwargs.get('surname')} {kwargs.get('name')}, {kwargs.get('year')} года рождения, "
          f"проживает в городе {kwargs.get('city')}, Эл.почта: {kwargs.get('email')} Телефон: {kwargs.get('phone')}")


user_func(name="Dmitriy", surname="Romashev", year=1975,
          city="Saint-Petersburg", email="romashev.dmitriy@gmail.com", phone="8-911-232-59-36")

