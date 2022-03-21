"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone():
    model: str
    brand: str
    issue_year: int
    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def __str__(self):
        return (f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}")

    #def __str__(self):
        #print(f"Бренд: {self.brand}")
        #print(f"Модель: {self.model}")
        #print(f"Год выпуска: {self.issue_year}")
        #return ок

    @staticmethod
    def receive_call (name):
        print(f"Звонит {name}")

    def get_info(self):
        info = (self.brand, self.model, self.issue_year)
        return info


phone1 = Phone('Sony', 'X5', 2019)
Phone.receive_call('Helen')
print(phone1.get_info())
print(type(phone1.get_info()))
print(str(phone1))

