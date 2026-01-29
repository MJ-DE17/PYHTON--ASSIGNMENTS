import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/StringFormatting")
    )
)

from util import get_formatted_numbers


class TestStringFormatting(unittest.TestCase):

    def test_small_input(self):
        self.assertEqual(
            get_formatted_numbers(2),
            [
                " 1  1  1  1",
                " 2  2  2 10"
            ]
        )

    def test_single_value(self):
        self.assertEqual(
            get_formatted_numbers(1),
            ["1 1 1 1"]
        )


if __name__ == "__main__":
    unittest.main()
