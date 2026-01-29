import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/PilingUp")
    )
)

from util import can_stack


class TestPilingUp(unittest.TestCase):

    def test_yes_case(self):
        self.assertTrue(can_stack([4, 3, 2, 1, 3, 4]))

    def test_no_case(self):
        self.assertFalse(can_stack([1, 3, 2]))


if __name__ == "__main__":
    unittest.main()
