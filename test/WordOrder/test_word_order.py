import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/WordOrder")
    )
)

from util import word_order


class TestWordOrder(unittest.TestCase):

    def test_sample(self):
        words = ["bcdef", "abcdefg", "bcde", "bcdef"]
        result = word_order(words)

        self.assertEqual(len(result), 3)
        self.assertEqual(list(result.values()), [2, 1, 1])


if __name__ == "__main__":
    unittest.main()
