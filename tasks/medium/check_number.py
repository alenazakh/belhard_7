"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    else:
        return check_number(n * 0.5)


print(check_number(8))
print(check_number(9))
print(check_number(256))
print(check_number(1))
