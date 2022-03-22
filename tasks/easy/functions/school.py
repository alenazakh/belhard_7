"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(class_name: str, **kwargs):
    kwargs[class_name] = kwargs.get(class_name) + 1
    return kwargs


def decr_students(class_name: str, **kwargs):
    kwargs[class_name] = kwargs.get(class_name) - 1
    return kwargs


def add_class(class_name: str, **kwargs):
    kwargs.update({class_name: 0})
    return kwargs


def remove_class(class_name: str, **kwargs):
    kwargs.pop(class_name)
    return kwargs


def calc_students(**kwargs):
    summa = 0
    for item in kwargs.values():
        summa = summa + item
    return summa


print(f"Первоначальный словарь: {school_data}")
school_data = incr_students('1a', **school_data)
school_data = decr_students('1b', **school_data)
school_data = add_class('1c', **school_data)
school_data = remove_class('2a', **school_data)
print(f"Измененный словарь: {school_data}")
print(calc_students(**school_data))
