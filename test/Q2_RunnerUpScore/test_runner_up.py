import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/Q2_RunnerUpScore")
    )
)

from src.StringFormatting.util import find_runner_up

class TestRunnerUpScore(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(find_runner_up([2, 3, 6, 6, 5]), 5)
    def test_negative_numbers(self):
        self.assertEqual(find_runner_up([-1, -2, -3, -1]), -2)


if __name__ == "__main__":
    unittest.main()
