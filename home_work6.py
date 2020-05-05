# Реализовать паттерн проектирования 'Прототип'
# Тематику выбирайте какую хотите (кафе, заводы, машины и прочее).
# В реализации пожеланий нет(функции, классы ...),
# главное чтобы решалась проблема описанная в паттерне


from random import randint
import copy
import sys


# Представим автоматическую базу на другой планете. Кроме всего барахла, на ней
# есть сборщик, который умеет собирать специализированных роботов на основе
# прототипа корпуса. В памяти сборщика есть две модели, менее затратная и менее
# прочная модель, и , соответсвенно, более дорогая, но и болие прочная.
class Prototype:
    """Наш класс прототипов"""

    def __init__(self):
        """Инициализация пустого словаря прототипов,
        где мы будем их регистрировать"""
        self.objects = {}

    def register_model(self, name, model):
        """Регистрация прототипа в словарь"""
        self.objects[name] = model

    def unregister_model(self, name):
        """Удаление прототипа из словаря"""
        del self.objects[name]
        print(f'{name} - удален, как неэффективный.')

    def clone(self, name, **kwargs):
        """Клонирование прототипа для сборки робота с задаваемыми параметрами"""
        obj = copy.deepcopy(self.objects[name])
        obj.__dict__.update(kwargs)
        return obj


class Vehicle:
    """Наш класс роботов"""

    def __init__(self, profession='empty', strength=0):
        """Инициализация робота с определением ему професии и модели корпуса"""
        self.profession = profession
        self.strength = strength

    def to_work(self, a):
        """Сборка робота для задания"""
        return prototype.clone(a, profession=self.profession)

    def work_and_return(self):
        """Удачное выполнение роботом функции"""
        print(f'{self.profession} - справился с заданием и вернулся.')

    def last_words(self):
        """Последнее сообщение при разрушении"""
        print(f"{self.profession} - был разрушен.")


# ф-ция генерирует повреждение от окружающей среды
def damage():
    return randint(50, 150)


prototype = Prototype()
# Регисрация моделей корпуса в каталог прототипов
prototype.register_model('vehicle1', Vehicle(strength=100))
prototype.register_model('vehicle2', Vehicle(strength=200))

# Инициализация типов роботов с определением их професий
scout = Vehicle(profession='scout')
miner = Vehicle(profession='miner')
fitter = Vehicle(profession='fitter')

# Список роботов и соответствующих корпусов
models_dict = {'scout': 'vehicle1', 'miner': 'vehicle1', 'fitter': 'vehicle1'}

# РАБОТА
run = ''
day = 0
while run != '0':
    day += 1
    run = input('run? yes / no = "y" / some else ')

    if run == 'y':
        work_list = [scout, miner, fitter]
        print(f'========день {day}========')

        for worker in work_list:
            worker = worker.to_work(models_dict[worker.profession])
            print(f'{worker.profession} собран для задания в корпусе '
                  f'с прочностью {worker.strength}')
            if worker.strength > damage():  # получение повреждений
                worker.work_and_return()
            else:
                worker.last_words()
                # если робот был разрущен, значит ему необходим корпус попрочнее
                models_dict[worker.profession] = 'vehicle2'
            print('----------------------------')
        print('============================')

        # если всем роботам необходим крпус попрочнее, значит более дешевый
        # себя не зарекомендовал и его необходимо удалить с каталога прототипов
        if 'vehicle1' not in models_dict.values() \
                and 'vehicle1' in prototype.objects:
            prototype.unregister_model('vehicle1')
    else:
        sys.exit()
