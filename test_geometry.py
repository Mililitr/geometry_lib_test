import unittest
from geometry import Circle, Triangle, calculate_area

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=5)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_not_right_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())

    def test_calculate_area_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483, places=5)

    def test_calculate_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0, places=5)

if __name__ == '__main__':
    unittest.main()