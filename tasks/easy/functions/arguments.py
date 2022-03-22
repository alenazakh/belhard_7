"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html

Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    func_result = {}
    if all(isinstance(item, int) for item in args) is True:
        args_sum = 0
        for i in range(len(args)):
            args_sum = args_sum + args[i]
        func_result.update({'args_sum': args_sum})
    else:
        raise TypeError("Все позиционные аргументы должны быть целыми.")
# dict_keys = kwargs.keys()
    if all(isinstance(item, str) for item in kwargs.keys()) is True:
        kwargs_max_len = 0
        for item in kwargs.keys():
            if kwargs_max_len < len(item):
                kwargs_max_len = len(item)
        func_result.update({'kwargs_max_len': kwargs_max_len})
    else:
        raise TypeError("се аргументы - ключевые слова должны быть строками.")
    return func_result


list1 = [1, 5, 6, 8]
list2 = ['1', 5, 6, 8]
dict1 = {'x1': 0, 'x22': 4, 'x333': 7, 'x4444': 6, 'x55555': 8}
dict2 = {'x1': 0, 'x22': '4', 3: 7, 'x4444': 6, 'x55555': "8"}
print(dict_from_args(*list1, **dict1))  # если словарь с ключами не строками, то ошибка выпадает сразу, заменить ее или в функцию добавить не получилось
