import unittest
from src.elastica import elastica_in_TI

class TestElastica(unittest.TestCase):

    def test_elastica_in_TI_circle(self):
        dx = 1.2247
        R = (3)**0.5
        result = elastica_in_TI(-dx, 0, 45, -1/R, dx, 0, -45, -1/R, 0.001, [0, 0, 0, (3)**0.5 * 3.14159 / 2], 1)
        self.assertIsNotNone(result)

    def test_elastica_in_TI_increasing_curvature(self):
        dx = 1.2247
        a = 0.3
        R = (3)**0.5
        result = elastica_in_TI(-dx, 0, 45, -1/R - a, dx, 0, -45, -1/R - a, 0.001, [0.15, -1.61, 0.75, 3.0244387], 1)
        self.assertIsNotNone(result)

    def test_elastica_in_TI_decreasing_curvature(self):
        dx = 1.2247
        a = -0.3
        R = (3)**0.5
        result = elastica_in_TI(-dx, 0, 45, -1/R - a, dx, 0, -45, -1/R - a, 0.001, [0.27, 1.37, -0.4, 2.77], 1)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()