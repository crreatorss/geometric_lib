import unittest 
from circle import *
from square import *
class TestCircleCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(2), 4 * math.pi)

    def test_perimeter(self):
        self.assertEqual(circle_perimeter(0), 0)
        self.assertAlmostEqual(circle_perimeter(1), 2*math.pi)
        self.assertAlmostEqual(circle_perimeter(2), 4*math.pi)

class TestSquareCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(1), 1)
        self.assertEqual(square_area(5), 25)

    def test_perimetr(self):
        self.assertEqual(square_perimeter(0), 0)
        self.assertEqual(square_perimeter(1), 4)
        self.assertEqual(square_perimeter(5), 20)

