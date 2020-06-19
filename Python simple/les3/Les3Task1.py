# Дан список. Выведите те его элементы, которые встречаются в списке
# только один раз. Элементы нужно выводить в том порядке,
# в котором они встречаются в списке.

some_list = [
    'q', 'd', 'f', 'r', 'd', 's', 'd', 'c', 'w', 'q', 'd', 't', 'u', 'i', 'x', 'v'
]

for i in range(len(some_list)):
    elem = some_list.pop(i)
    if elem not in some_list:
        print(elem)
        some_list.insert(i, elem)
    else:
        some_list.insert(i, elem)

# другой вариант
# print([elem for elem in some_list if some_list.count(elem) == 1])
