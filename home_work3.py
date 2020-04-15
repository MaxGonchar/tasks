# 1. Написать функцию, которая будет принимать на вход натуральное число n,
# и возращать сумму его цифр. Реализовать используя рекурсию
# (без циклов, без строк, без контейнерных типов данных).
# Пример: get_sum_of_components(123) -> 6 (1+2+3)
def sum_digits(n):
    n = abs(n)
    if n // 10 == 0:
        return n % 10
    else:
        return (n % 10) + sum_digits(n // 10)


# 2. Написать декоратор log, который будет выводить на экран все аргументы,
# которые передаются вызываемой функции.
# @log
# def my_sum(*args):
# return sum(*args)
#
# my_sum(1,2,3,1) - выведет "Функция была вызвана с - 1, 2, 3, 1"
# my_sum(22, 1) - выведет "Функция была вызвана с - 22, 1"
def log(some_func):
    def wrapper(*args):
        print('Функция была вызвана с - ', end='')
        for a in zip(list(map(str, args)), [', '] * (len(args) - 1) + ['']):
            print(''.join(list(a)), end='')
        return some_func(*args)

    return wrapper


@log
def my_sum(*args):
    return sum(args)


# my_sum(1, 2, 3, 1)
if __name__ == '__main__':
    # TASK 1
    assert sum_digits(11111) == 5
    assert sum_digits(15654654) == 36
    assert sum_digits(-15654654) == 36

    # TASK 2
    assert my_sum(1, 2, 3, 1) == 7
    print()
    assert my_sum(22, 1) == 23
