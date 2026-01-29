import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/Q1_StudentAverage")
    )
)

from src.StringFormatting.util import calculate_average


class TestStudentAverage(unittest.TestCase):

    def test_average_int_marks(self):
        self.assertEqual(calculate_average([52, 56, 60]), 56.0)

    def test_average_float_marks(self):
        self.assertEqual(calculate_average([25, 26.5, 28]), 26.5)


if __name__ == "__main__":
    unittest.main()
