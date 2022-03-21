"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'

def count_char(STR_VAL):
    str_val_list = list(STR_VAL)
    unique = []
    for item in str_val_list:
        if item not in unique:
            unique.append(item)
    result = {}
    for item in unique:
        result.update({item: str_val_list.count(item)})
    return result

print(count_char(STR_VAL))

