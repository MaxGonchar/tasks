# Создать функцию, которая печатает одновременно
# ключ и значение полученного словаря. (Метод items)


# print keys and values of given dict
def kay_and_value(some_dict):
    for k, v in some_dict.items():
        print(f'{k}: {v}')


one_dict = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

kay_and_value(one_dict)
