import unittest
from src.utils.interpolation import poly_interpolation
from src.utils.curvature import find_curvature_from_points

class TestUtils(unittest.TestCase):

    def test_poly_interpolation(self):
        X = [0, 1, 2, 3, 4]
        Y = [0, 1, 4, 9, 16]
        ax, ay = poly_interpolation(X, Y)
        self.assertEqual(len(ax), 201)  # Check the number of points
        self.assertAlmostEqual(ay[0], 0)  # Check the first value
        self.assertAlmostEqual(ay[-1], 16)  # Check the last value

    def test_find_curvature_from_points(self):
        x0, y0 = 0, 0
        x1, y1 = 1, 1
        x2, y2 = 2, 0
        kappa, theta, circ = find_curvature_from_points(x0, y0, x1, y1, x2, y2)
        self.assertIsNotNone(kappa)  # Check that curvature is computed
        self.assertIsNotNone(theta)  # Check that angle is computed
        self.assertEqual(len(circ), 628)  # Check the number of points in the circle

if __name__ == '__main__':
    unittest.main()