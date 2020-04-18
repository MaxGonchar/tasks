# Реализовать некий класс Matrix, у которого:
# 1. Есть собственный конструктор, который принимает в качестве аргумента -
#    список списков, копирует его (то есть при изменении списков,
#    значения в экземпляре класса не должны меняться).
#    Элементы списков гарантированно числа, и не пустые.
# 2. Метод size без аргументов, который возвращает кортеж вида
#    (число строк, число столбцов).
# 3. Метод transpose, транспонирующий матрицу и возвращающую результат
#    (данный метод модифицирует экземпляр класса Matrix)
# 4. На основе пункта 3 сделать метод класса create_transposed,
#    который будет принимать на вход список списков, как и в пункте 1,
#    но при этом создавать сразу транспонированную матрицу.


def output(array: list, text: str):
    print(text)
    for i in range(len(array)):
        print(array[i])
    print()


class Matrix:
    def __init__(self, bag_of_bags: list):
        self.bag_of_bags = bag_of_bags.copy()

    def size(self):
        m = len(self.bag_of_bags)
        n = len(self.bag_of_bags[0])
        return m, n

    def transpose(self):
        t_arr = list(map(list, (zip(*self.bag_of_bags))))
        return t_arr

    @classmethod
    def create_transposed(cls, matr):
        t_matr = list(map(list, (zip(*matr))))
        return cls(t_matr)


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output(arr, 'Исходная матрица')

matrix_1 = Matrix(arr)
output(matrix_1.bag_of_bags, 'Значения в экземпляре класса')

arr.append([10, 11, 12])
output(arr, 'Меняем исходную матрицу')
output(matrix_1.bag_of_bags, 'Значения в экземпляре класса')


print(f'Размер матрици (стр, столб) {matrix_1.size(), type(matrix_1.size())}\n')

output(matrix_1.transpose(), 'Транспонированная матрица')

matrix_2 = Matrix.create_transposed(arr)
output(matrix_2.bag_of_bags, 'Матрица в новом экземпляре, созданном classmethod')
