"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.
Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
Определить атрибуты:
- value - текущее значение счетчика
Определить методы:
- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""

class Counter():
    def __init__(self, value=0, end = 2147483647):
        self.value = value
        self.end = end


    def __iter__(self):
        self.list = ()
        while self.value <= self.end:
            self.list.append(self.value)
        return self.list


    def __next__(self):
        index=0
        for index in range(len(self.list)):
            return self.list[index]


    def increase(self):
        while self.value < self.end:
            self.value += 1
            yield self.value


    def decrease(self):
        while self.value > 0:
            self.value -= 1
            yield self.value

counter1 = Counter(4,13)
counter01 = counter1.increase()
print(next(counter01))
print(next(counter01))
print(next(counter01))
print(next(counter01))
print(next(counter01))
print(next(counter01))
print(next(counter01))
print(next(counter01))


