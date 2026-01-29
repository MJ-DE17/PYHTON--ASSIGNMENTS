import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/NamedTupleAverage")
    )
)

from util import average_marks


class TestNamedTupleAverage(unittest.TestCase):

    def test_sample_case(self):
        n = 5
        fields = ["ID", "MARKS", "NAME", "CLASS"]
        rows = [
            ["1", "97", "Raymond", "7"],
            ["2", "50", "Steven", "4"],
            ["3", "91", "Adrian", "9"],
            ["4", "72", "Stewart", "5"],
            ["5", "80", "Peter", "6"],
        ]
        self.assertEqual(average_marks(n, fields, rows), 78.00)


if __name__ == "__main__":
    unittest.main()
