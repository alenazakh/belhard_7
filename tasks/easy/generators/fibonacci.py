"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci():
    num1 = 0
    yield num1
    num2 = 1
    yield num2
    while True:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        yield num3


fibonacci_gen = fibonacci()
print(f"next: {next(fibonacci_gen)}")
print(f"next: {next(fibonacci_gen)}")
print(f"next: {next(fibonacci_gen)}")
print(f"next: {next(fibonacci_gen)}")
print(f"next: {next(fibonacci_gen)}")
print(f"next: {next(fibonacci_gen)}")
print(f"next: {next(fibonacci_gen)}")
print(f"next: {next(fibonacci_gen)}")