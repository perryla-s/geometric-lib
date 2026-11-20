import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    def test_area_normal(self):
        '''Проверка площади квадрата со стороной 5'''
        self.assertEqual(area(5), 25)

    def test_area_zero(self):
        '''Проверка площади квадрата со стороной 0'''
        self.assertEqual(area(0), 0)

    def test_perimeter_normal(self):
        '''Проверка периметра квадрата со стороной 5'''
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_zero(self):
        '''Проверка периметра квадрата со стороной 0'''
        self.assertEqual(perimeter(0), 0)

if __name__ == '__main__':
    unittest.main()