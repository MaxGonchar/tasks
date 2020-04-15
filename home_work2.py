# -*- coding: utf-8 -*-
import random


# 1. Определить количество четных и нечетных чисел в заданном списке.
# Оформить в виде функции, где на вход будет подаваться список с целыми числами.
# Результат функции должен быть 2 числа, кол-во четных и нечетных соответственно.
def even_odd(seq):
    even, odd = 0, 0
    for n in seq:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# 2. Написать функцию, которая принимает 2 числа. Функция должна вернуть сумму
# всех элементов числового ряда между этими двумя числами.
# (если подать 1 и 5 на вход, то результат должен считаться как 1+2+3+4+5 = 15)
def amount(a, b):
    s = sum([n for n in range(a, b + 1)])
    return s


# 3. Реализовать алгоритм бинарного поиска на python.
# На вход подается упорядоченный список целых чисел, а так же элемент,
# который необходимо найти и указать его индекс, в противном случае –
# указать что такого элемента нет в заданном списке.
def binary_search(seq, elem):
    first, last = 0, len(seq) - 1
    while first <= last:
        mid = (last + first) // 2
        if elem > seq[mid]:
            first = mid + 1
        elif elem < seq[mid]:
            last = mid - 1
        elif elem == seq[mid]:
            return mid
    else:
        return None


print('TASK 1')
sequence_1 = [random.randint(1, 10) for i in range(10)]
print(f'In sequence {sequence_1}\n'
      f'even numbers - {even_odd(sequence_1)[0]}\n'
      f'odd numbers - {even_odd(sequence_1)[1]}\n')

print('TASK 2')
x = random.randint(0, 10)
y = random.randint(11, 20)
print(f'Sum of all elements between {x} and {y} inclusive is {amount(x, y)}\n')

print('TASK 3')
sequence_2 = sorted(list(set([random.randint(1, 10) for _ in range(10)])))
element = random.randint(1, 10)
print(f' In sequence {sequence_2}\n'
      f'index of element {element} is {binary_search(sequence_2, element)}')