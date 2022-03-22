"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number(start=0):                  # можно завести end для конечности цикла
    if start == 0:
        start = start
    elif start % 2 == 1:
        start = start - 1
    elif start % 2 == 0:
        start = start - 2
    while True:                              # если завести end то будет проверка на больше 0 меньше end
        start += 2
        yield start


even_gen = get_even_number()
print(f"next: {next(even_gen)}")
print(f"next: {next(even_gen)}")
print(f"next: {next(even_gen)}")
