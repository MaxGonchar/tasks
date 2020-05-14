# -*- coding: utf-8 -*-
# 1. Реализовать подсчёт елементов в классе Matrix с помощью collections.Counter.
#    Можно реализовать протоколом итератора и тогда будет такой вызов -
#    Counter(maxtrix). Либо сделать какой-то метод get_counter(),
#    который будет возвращать объект Counter и подсчитывать все элементы
#    внутри матрицы. Какой метод - ваш выбор.
from typing import List, Union
from collections import Counter


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

    def __iter__(self) -> iter:
        """Iterator for elementwise iteration"""
        return iter(sum(self.bag_of_bags, []))

    def get_counter(self) -> Counter:
        """
        Method counts number of matrix's elements and return Counter object
        """
        c = Counter()
        for line in self.bag_of_bags:
            c += Counter(line)
        return c


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 0]])

    print(matrix1.get_counter())
    print(Counter(iter(matrix2)))
