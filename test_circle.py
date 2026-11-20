import math
import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_area_normal(self):
        '''Проверка площади круга с радиусом 3'''
        self.assertAlmostEqual(area(3), math.pi * 9)

    def test_area_zero(self):
        '''Проверка площади круга с нулевым радиусом'''
        self.assertEqual(area(0), 0)

    def test_perimeter_normal(self):
        '''Проверка длины окружности с радиусом 3'''
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)

    def test_perimeter_zero(self):
        '''Проверка длины окружности с нулевым радиусом'''
        self.assertEqual(perimeter(0), 0)

if __name__ == '__main__':
    unittest.main()