"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(*args):
    args = list(args[0])
    if all(isinstance(item, int) for item in args) is True:
        list0 = []
        for i in range(len(args)):
            if args[i] in list0:
                print("Yes")
            else:
                print("No")
            list0.append(args[i])


# raise TypeError(f'В списке не все целые числа! Функция принимает только целые числа.')


list1 = [1, 2, 3, 2, 5, 6, 1, 7]
yes_or_no(list1)
# yes_or_no(1,3,4,5,4,3,'18')
