# -*- coding: utf-8 -*-
#  Используя модуль unittests написать тесты: сложения двух матриц,
#  умножения матрицы и метод transpose

import unittest

import homework7


class MatrixTest(unittest.TestCase):
    """Class of tests with given data"""
    matrix1 = homework7.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = homework7.Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 0]])
    matrix3 = homework7.Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 0], [4, 5, 6]])

    def test_add_equal(self):
        """addition test for 'add'"""
        self.assertEqual((MatrixTest.matrix1 + MatrixTest.matrix2).bag_of_bags,
                         ([[3, 5, 7], [9, 11, 13], [15, 17, 9]]))

    def test_add_error(self):
        """error test for 'add'"""
        with self.assertRaises(IOError):
            a = MatrixTest.matrix1 + MatrixTest.matrix3

    def test_add_type(self):
        """type matching test for 'add'"""
        self.addTypeEqualityFunc(
            homework7.Matrix,
            (MatrixTest.matrix1 + MatrixTest.matrix2))

    def test_mul_equal(self):
        """multiplication test for 'mul'"""
        self.assertEqual((MatrixTest.matrix1 * 2).bag_of_bags,
                         [[2, 4, 6], [8, 10, 12], [14, 16, 18]])

    def test_mul_type(self):
        """type matching test for 'mul'"""
        self.addTypeEqualityFunc(homework7.Matrix, (MatrixTest.matrix1 * 2))

    def test_transpose_equal(self):
        """transpose test for 'transpose'"""
        self.assertEqual(MatrixTest.matrix1.transpose(),
                         [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_transpose_type(self):
        """class instance change confirmation test for 'transpose'"""
        before_id = id(MatrixTest.matrix1)
        MatrixTest.matrix1.transpose()
        after_id = id(MatrixTest.matrix1)

        self.assertEqual(before_id, after_id)
