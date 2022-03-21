"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""
def fibonacci(num_count):
    try:
        if num_count > 1:
            num1 = 0
            #yield num1
            num2 = 1
            yield num2
            count_limit = 2
            while count_limit <= num_count:
                num3 = num1 + num2
                num1 = num2
                num2 = num3
                count_limit +=1
                yield num3
        else:
            raise ValueError(f'Введите значение больше 1.')
    except StopIteration as exc:
        print(f'Итерируемые данные закончились.')


#fibonacci_gen = fibonacci(0)
#print(next(fibonacci_gen))
fibonacci_gen = fibonacci(5)
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))


