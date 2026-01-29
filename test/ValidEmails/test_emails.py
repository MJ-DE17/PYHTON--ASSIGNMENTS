import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/ValidEmails")
    )
)

from util import is_valid_email


class TestEmails(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(is_valid_email("brian-23@hackerrank.com"))

    def test_invalid_extension(self):
        self.assertFalse(is_valid_email("test@site.comm"))

    def test_invalid_username(self):
        self.assertFalse(is_valid_email("test!@site.com"))


if __name__ == "__main__":
    unittest.main()
