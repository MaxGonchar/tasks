# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным.
# Если год является високосным, то выведите YES,
# иначе выведите NO.
# В соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

try:
    x = int(input('Введите год '))
except ValueError:
    print('Год введен некорректно')
else:
    if (x % 400 == 0) or (x % 4 == 0 and not (x % 100 == 0)):
        print('YES')
    else:
        print('NO')
finally:
    print('final')