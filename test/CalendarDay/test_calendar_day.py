import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/CalendarDay")
    )
)

from util import find_day


class TestCalendarDay(unittest.TestCase):

    def test_sample_date(self):
        self.assertEqual(find_day(8, 5, 2015), "WEDNESDAY")

    def test_new_year(self):
        self.assertEqual(find_day(1, 1, 2000), "SATURDAY")


if __name__ == "__main__":
    unittest.main()
