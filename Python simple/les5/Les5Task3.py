# Мини игра
# Скрипт создаёт случайное число, неизвестное для пользователя.
# И просит у пользователя угадать его(победа) с ограничением в 3 попытки(проигрыш).
# Дополнительно можно запилить подсказки "горячо/холодно"

import random

x = random.randint(1, 100)

print('I made a number from 1 to 100')

a = int(input('try to guess - '))
if a == x:
    print('you won')
else:
    dif = abs(a - x)
    for i in range(2):
        a = int(input('try again - '))
        if a == x:
            print('you won')
            break
        else:
            if abs(a - x) < dif:
                print('warmer')
            elif abs(a - x) > dif:
                print('colder')
    else:
        print('you lost, the number was - ', x)
