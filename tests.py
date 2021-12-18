import unittest
from hw3 import minimum_of_nums
from hw3 import maximum_of_nums
from hw3 import sum_of_nums
from hw3 import multiplication_of_nums


class Tests(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum_of_nums([5.0, -0.0, 2.5]), 0)
        self.assertEqual(minimum_of_nums([-5.3, 1.2, 1.1]), -5.3)
        self.assertEqual(minimum_of_nums([-0.1, 0.01, -0.001]), -0.1)
        self.assertEqual(minimum_of_nums([1.0, 8.3, 1.001]), 1)
        self.assertEqual(minimum_of_nums([-9.0, -123.6, -123.5]), -123.6)

    def test_maximum(self):
        self.assertEqual(maximum_of_nums([5.0, -0.0, 2.5]), 5)
        self.assertEqual(maximum_of_nums([-5.3, 1.2, 1.1]), 1.2)
        self.assertEqual(maximum_of_nums([-0.1, -0.01, -0.001]), -0.001)
        self.assertEqual(maximum_of_nums([1.0, 8.3, 8.0]), 8.3)
        self.assertEqual(maximum_of_nums([-9.0, -123.6, -9.1]), -9)

    def test_summa(self):
        self.assertEqual(sum_of_nums([5.0, -0.0, -5.0]), 0)
        self.assertEqual(sum_of_nums([-5.3, 1.2, 1.1]), -3)
        self.assertEqual(sum_of_nums([-0.1, -0.01, -0.001]), -0.111)
        self.assertEqual(sum_of_nums([1.0, 8.3, 8.0]), 17.3)
        self.assertEqual(sum_of_nums([-9.0, -123.6, -9.1]), -141.7)

    def test_multiplication(self):
        self.assertEqual(multiplication_of_nums([5.0, -0.0, -5.0]), 0)
        self.assertEqual(multiplication_of_nums([-5.3, 1.2, -2.0]), 12.72)
        self.assertEqual(multiplication_of_nums([-0.1, -0.01, -0.001]), -0.000001)
        self.assertEqual(multiplication_of_nums([4.0, 4.0, 4.0]), 64)
        self.assertEqual(multiplication_of_nums([-3.0, -3.0, -3.0]), -27)
