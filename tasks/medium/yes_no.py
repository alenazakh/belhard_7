"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""

def yes_or_no(*args):
    if all(isinstance(item, int) for item in args) is True:
        list0 = []
        for i in range(len(args)):
            if args[i] in list0:
                print("Yes")
            else: print("No")
            list0.append(args[i])
    else:
        #raise TypeError(f'В списке не все целые числа! Функция принимает только целые числа.')
        pass



yes_or_no(1,3,4,5,4,3,18)
#yes_or_no(1,3,4,5,4,3,'18')
