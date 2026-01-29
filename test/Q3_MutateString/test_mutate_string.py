import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/Q3_MutateString")
    )
)

from util import mutate_string


class TestMutateString(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(
            mutate_string("abracadabra", 5, "k"),
            "abrackdabra"
        )

    def test_first_index(self):
        self.assertEqual(
            mutate_string("hello", 0, "y"),
            "yello"
        )


if __name__ == "__main__":
    unittest.main()