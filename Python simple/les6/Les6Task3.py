# Создать функцию, которая принимает строку и возвращает один словарь
# со "счётчиками". Счётчики отвечают за количество
# цифр/букв/пробелов/знаков препинания в полученной строке.

def comp_str(s):
    num_of_alpha = 0
    num_of_digit = 0
    num_of_space = 0
    other_num = 0
    dict_of_simbols = {'litters': num_of_alpha,
                       'numbers': num_of_digit,
                       'spaces': num_of_space,
                       'other': other_num}

    for i in range(len(s)):
        if s[i].isalpha():
            num_of_alpha += 1
            dict_of_simbols['litters'] = num_of_alpha
        elif s[i].isdigit():
            num_of_digit += 1
            dict_of_simbols['numbers'] = num_of_digit
        elif s[i] == ' ':
            num_of_space += 1
            dict_of_simbols['spaces'] = num_of_space
        else:
            other_num += 1
            dict_of_simbols['other'] = other_num

    return dict_of_simbols


some_string = '''Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24)
[MSC v.1916 32 bit (Intel)] on win32'''
for k, v in comp_str(some_string).items():
    print(f'{k}: {v}')
