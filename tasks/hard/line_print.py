"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на 4 пробела

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


def line_print(some_list, count=0):
    for item in some_list:
        if isinstance(item, list):
            line_print(item, count + 1)
        else:
            print(" " * 4 * count + str(item))


list1 = [1, 2, [3, 4, [5, 6], 7, 8], 9, 10]
line_print(list1)
some_list = [1, [2], [1, [2], [5, 7], 3], 8]
line_print(some_list)
