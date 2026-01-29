import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/ProbabilityA")
    )
)

from util import probability_of_a


class TestProbability(unittest.TestCase):

    def test_sample(self):
        letters = ['a', 'a', 'c', 'd']
        self.assertEqual(probability_of_a(letters, 2), 0.8333)


if __name__ == "__main__":
    unittest.main()
