import unittest
import sys
import os
import numpy as np

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/MeanVarStd")
    )
)

from util import mean_var_std


class TestMeanVarStd(unittest.TestCase):

    def test_sample(self):
        arr = np.array([[1, 2], [3, 4]])
        mean, var, std = mean_var_std(arr)

        self.assertTrue((mean == np.array([1.5, 3.5])).all())
        self.assertTrue((var == np.array([1., 1.])).all())
        self.assertAlmostEqual(std, 1.11803398875)


if __name__ == "__main__":
    unittest.main()
