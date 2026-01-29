import unittest
import sys
import os
import numpy as np

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/FloorCeilRint")
    )
)

from util import floor_ceil_rint


class TestFloorCeilRint(unittest.TestCase):

    def test_basic(self):
        arr = np.array([1.1, 2.2, 5.5])
        f, c, r = floor_ceil_rint(arr)

        self.assertTrue((f == np.array([1., 2., 5.])).all())
        self.assertTrue((c == np.array([2., 3., 6.])).all())
        self.assertTrue((r == np.array([1., 2., 6.])).all())


if __name__ == "__main__":
    unittest.main()
