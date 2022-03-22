"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


result = []


def sum_of_numbers(number):
    if number == 0:
        return sum(result)
    else:
        result.append(number % 10)
        return sum_of_numbers(number // 10)


print(sum_of_numbers(123))
