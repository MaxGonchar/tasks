# К реализованному классу Matrix в Домашнем задании 3 добавить следующее:
# 1. __add__ принимающий второй экземпляр класса Matrix и возвращающий сумму
#   матриц, если передалась на вход матрица другого размера - поднимать
#   исключение MatrixSizeError (по желанию реализовать так, чтобы текст ошибки
#   содержал размерность 1 и 2 матриц - пример:
#   "Matrixes have different sizes - Matrix(x1, y1) and Matrix(x2, y2)")
# 2. __mul__ принимающий число типа int или float и возвращающий матрицу,
#   умноженную на скаляр/
# 3. __str__ переводящий матрицу в строку. Столбцы разделены между собой
#   табуляцией, а строки — переносами строк (символ новой строки). При этом после
#   каждой строки не должно быть символа табуляции и в конце не должно быть
#   переноса строки.
from typing import List, Union


class Matrix:
    """Some class"""

    def __init__(self, bag_of_bags: List[list]) -> None:
        self.bag_of_bags = bag_of_bags.copy()

    def size(self) -> tuple:
        """Method witch returns number of strings as 'm'
           and number of columns as 'n' in self instance's matrix"""
        m = len(self.bag_of_bags)
        n = len(self.bag_of_bags[0])
        return m, n

    def transpose(self) -> List[list]:
        """Method witch returns transposed self instance's matrix"""
        self.bag_of_bags = list(map(list, (zip(*self.bag_of_bags))))
        return self.bag_of_bags

    @classmethod
    def create_transposed(cls, matr) -> 'Matrix':
        """Method witch creates class's instance
           by transposing the received matrix """
        t_matr = list(map(list, (zip(*matr))))
        return cls(t_matr)

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Addition of self matrix with other matrix.
           If matrices sizes are different -> raise 'MatrixSizeError' """
        if self.size() == other.size():
            rez = [[el1 + el2 for el1, el2 in zip(bag1, bag2)]
                   for bag1, bag2 in zip(self.bag_of_bags, other.bag_of_bags)]
        else:
            raise IOError(f'MatrixSizeError:\n matrixes have different sizes -'
                          f' matrix1 {self.size()} and matrix2 {other.size()}')
        return Matrix(rez)

    def __mul__(self, other: Union[int, float]) -> 'Matrix':
        """Multiplies the matrix by a scalar number"""
        rez = [[el * abs(other) for el in bag] for bag in self.bag_of_bags]
        return Matrix(rez)

    def __str__(self) -> str:
        """Turn matrix to string,
           where between columns is '\t', between strings is '\n'."""
        return '\n'.join(['\t'.join([str(el) for el in bag])
                          for bag in self.bag_of_bags])


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 0]])

print(f'matrix1 -> str\n'
      f'{str(matrix1)}\n')

print(f'matrix1\n'
      f'{str(matrix1)}\n'
      f'matrix2\n'
      f'{str(matrix2)}\n'
      f'matrix1 + matrix2\n'
      f'{str(matrix1 + matrix2)}\n')

# for Error
# matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrix2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 0], [1, 1, 1]])
#
# matrix3 = matrix1 + matrix2

print(f'matrix1\n'
      f'{str(matrix1)}\n'
      f'matrix1 * 2\n'
      f'{matrix1 * 2}\n')
