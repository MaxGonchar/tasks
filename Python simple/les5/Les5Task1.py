# Функция принимает строчку и определяет корректно ли открыты/закрыты скобки.
# При этом в строке помимо скобок могут быть цифры/буквы/арифметические знаки.
# Возвращает булево значение.
# Пример
# (1+2)*(1-6) правда
# ((5+5)-7+7*8+(14/2) неправда

def correct_parentheses(some_string):
    resalt = True
    par_example = ['(', ')', '[', ']', '{', '}']
    par_only = ''
    for i in some_string:
        if i in par_example:
            par_only = par_only + i

    cheack_str = ''
    while len(cheack_str) != len(par_only):
        cheack_str = par_only
        par_only = par_only.replace('()', '')
        par_only = par_only.replace('[]', '')
        par_only = par_only.replace('{}', '')
    if len(cheack_str) != 0:
        resalt = False

    return resalt


s1 = '(     )      [     }     [   (   )    (    )      }'
s2 = '(    (   (    {   }[    ]   )   )    {    }     [    ]     )'
print(correct_parentheses(s1))
print(correct_parentheses(s2))
