import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/Q4_MergeTheTools")
    )
)

from util import merge_the_tools


class TestMergeTheTools(unittest.TestCase):

    def test_sample_case(self):
        self.assertEqual(
            merge_the_tools("AABCAAADA", 3),
            ["AB", "CA", "AD"]
        )

    def test_all_same_chars(self):
        self.assertEqual(
            merge_the_tools("AAAA", 2),
            ["A", "A"]
        )


if __name__ == "__main__":
    unittest.main()
