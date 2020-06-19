# Создать функцию которая возвращает 4 рандомных множества.
# И функцию которая возвращает количество общих элементов для этих сетов.


def rand_set(n):  # list of sets of random numbers in range(0,n)
    import random
    list_of_sets = [{random.randint(0, n) for i in range(n)} for j in range(4)]
    return list_of_sets


def set_intersect(some_list):  # intersection of sets
    inter_set = some_list[0]
    for i in range(1, len(some_list)):
        inter_set = inter_set & some_list[i]
    return inter_set


print(set_intersect(rand_set(100)))
