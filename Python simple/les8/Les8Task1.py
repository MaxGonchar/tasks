# Запилите скрипт, который при каждом запуске делает в файле запись формата:
# Порядковый номер - timestamp записи - переданные в скрипт аргументы.
#
# Учесть момент что файла при первом запуске скрипта может не быть

import datetime
import os
import sys

param = sys.argv[-1]
counter = 1
print('hi')

if os.path.isfile('test_file.txt'):
    with open('test_file.txt', 'r') as test_file:
        data = test_file.readlines()
        counter = int(data[-1].split(' ')[0]) + 1
    with open('test_file.txt', 'a') as test_file:
        test_file.write(str(counter) + ' '
                        + str(datetime.datetime.now()) + ' '
                        + str(param) + '\n')

else:
    with open('test_file.txt', 'a') as test_file:
        test_file.write(str(counter) + ' '
                        + str(datetime.datetime.now()) + ' '
                        + str(param) + '\n')
