"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    i = 1
    yield i
    while True:
        i = i * (i + 1)
        yield i


factorial_gen = factorial()
print(f"next: {next(factorial_gen)}")
print(f"next: {next(factorial_gen)}")
print(f"next: {next(factorial_gen)}")
print(f"next: {next(factorial_gen)}")
print(f"next: {next(factorial_gen)}")
