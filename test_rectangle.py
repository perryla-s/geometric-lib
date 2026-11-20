import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_area_normal(self):
        '''Проверка площади для стандартных положительных сторон'''
        self.assertEqual(area(5, 10), 50)

    def test_area_square(self):
        '''Проверка площади при равных сторонах'''
        self.assertEqual(area(10, 10), 100)

    def test_area_zero(self):
        '''Проверка площади при нулевой стороне'''
        self.assertEqual(area(10, 0), 0)

    def test_perimeter_normal(self):
        '''Проверка периметра для стандартных положительных сторон'''
        self.assertEqual(perimeter(5, 10), 30)

    def test_perimeter_zero(self):
        '''Проверка периметра при нулевых сторонах'''
        self.assertEqual(perimeter(0, 0), 0)


if __name__ == '__main__':
    unittest.main()