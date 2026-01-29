import unittest
import sys
import os
import numpy as np

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/Determinant")
    )
)

from util import determinant


class TestDeterminant(unittest.TestCase):

    def test_zero_determinant(self):
        mat = np.array([[1.1, 1.1], [1.1, 1.1]])
        self.assertEqual(determinant(mat), 0.0)

    def test_non_zero(self):
        mat = np.array([[1, 2], [2, 1]])
        self.assertEqual(determinant(mat), -3.0)


if __name__ == "__main__":
    unittest.main()
