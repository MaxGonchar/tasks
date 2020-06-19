# Регулярка для поиска автомобильных номеров формата АЕ1234ВА

import re
import random


# function generate random car number
def rand_numb():
    r_numb = (chr(random.randint(1040, 1071)) + chr(random.randint(1040, 1071))
              + str(random.randint(1000, 9999))
              + chr(random.randint(1040, 1071)) + chr(random.randint(1040, 1071)))
    return r_numb


# function generate string of  'a' random simbols, among wich meet
# random cars numbers with 10% probability
def rand_str(a):
    r_str = ''
    for i in range(0, a):
        if random.randint(0, 100) < 10:
            r_str += rand_numb()
        else:
            r_str += chr(random.randint(1040, 1103))
    return r_str


s = rand_str(100)
print(s)

car_numbers = re.findall('\w[А-Я]\d{4}\w[А-Я]', s)

for i in range(0, len(car_numbers)):
    print(car_numbers[i])
