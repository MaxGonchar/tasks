# Реализовать паттерн проектирования 'Прототип'
# Тематику выбирайте какую хотите (кафе, заводы, машины и прочее).
# В реализации пожеланий нет(функции, классы ...),
# главное чтобы решалась проблема описанная в паттерне
import copy
from random import randint


class Prototype:

    def __init__(self):
        self.objects = {}

    def register_model(self, name, model):
        self.objects[name] = model

    def unregister_model(self, name):
        del self.objects[name]
        print(f'{name} - deleted')

    def clone(self, name, **kwargs):
        obj = copy.deepcopy(self.objects[name])
        obj.__dict__.update(kwargs)
        return obj


class Vehicle:

    def __init__(self, profession='empty', strength=0):
        self.profession = profession
        self.strength = strength

    def to_work(self, a):
        return prototype.clone(a, profession=self.profession)

    def work_and_return(self):
        print(f'{self.profession} - Job is done')

    def last_words(self):
        print(f"{self.profession} - I'm ruined")


def damage():
    return randint(50, 150)


prototype = Prototype()
prototype.register_model('vehicle1', Vehicle(strength=100))
prototype.register_model('vehicle2', Vehicle(strength=200))

scout = Vehicle(profession='scout')
miner = Vehicle(profession='miner')
fitter = Vehicle(profession='fitter')

models_dict = {'scout': 'vehicle1', 'miner': 'vehicle1', 'fitter': 'vehicle1'}

run = ' '
while run != '0':
    run = input('run?')
    work_list = [scout, miner, fitter]

    for worker in work_list:
        worker = worker.to_work(models_dict[worker.profession])
        print(worker.profession, worker.strength)
        if worker.strength > damage():
            worker.work_and_return()
        else:
            worker.last_words()
            models_dict[worker.profession] = 'vehicle2'
        print('----------------------------')
    print('============================')
