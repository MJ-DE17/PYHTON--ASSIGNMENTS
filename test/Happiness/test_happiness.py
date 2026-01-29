import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/Happiness")
    )
)

from util import calculate_happiness


class TestHappiness(unittest.TestCase):

    def test_sample(self):
        arr = [1, 5, 3]
        A = {3, 1}
        B = {5, 7}
        self.assertEqual(calculate_happiness(arr, A, B), 1)


if __name__ == "__main__":
    unittest.main()
