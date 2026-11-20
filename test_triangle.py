import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        '''Проверка площади треугольника с основанием 10 и высотой 5'''
        self.assertEqual(area(10, 5), 25)

    def test_area_zero(self):
        '''Проверка площади треугольника при нулевой высоте'''
        self.assertEqual(area(10, 0), 0)

    def test_perimeter_normal(self):
        '''Проверка периметра треугольника со сторонами 3, 4, 5'''
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero(self):
        '''Проверка периметра треугольника с нулевыми сторонами'''
        self.assertEqual(perimeter(0, 0, 0), 0)

if __name__ == '__main__':
    unittest.main()