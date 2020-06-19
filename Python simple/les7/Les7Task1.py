# C помощью декораторов симетировать бутерброд. И добавить в декорируемую(там где хлеб)
# функцию "специи" при помощи args, если они есть - вывести на экран,
# если нет - "специй нет".


def sausage(s_func):
    def wrapper(*args):
        print('sausage')
        s_func(*args)

    return wrapper


def cheese(s_func):
    def wrapper(*args):
        print('cheese')
        s_func(*args)

    return wrapper


def butter(s_func):
    def wrapper(*args):
        print('butter')
        s_func(*args)

    return wrapper


@sausage
@cheese
@butter
def bread(*args):
    print('bread with ', *args)


a = ''
b = ''
c = ''
d = ''

if input('Want to add pepper y/n ') == 'y':
    a = 'pepper'
if input('Want to add paprica y/n ') == 'y':
    b = 'paprica'
if input('Want to add solt y/n ') == 'y':
    c = 'solt'
if a != 'pepper' and b != 'paprica' and c != 'solt':
    d = 'no spices'
bread(a, b, c, d)
