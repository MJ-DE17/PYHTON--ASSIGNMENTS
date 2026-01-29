import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/HackerRankLogo")
    )
)

from util import generate_logo


class TestHackerRankLogo(unittest.TestCase):

    def test_thickness_3(self):
        output = generate_logo(3)

        # correct total line count
        self.assertEqual(len(output), 16)

        # basic pattern checks
        self.assertIn("H", output[0])       # top cone
        self.assertIn("HHHHH", output[7])   # middle belt

    def test_thickness_5(self):
        output = generate_logo(5)

        self.assertTrue(output[0].strip().startswith("H"))
        self.assertTrue(output[-1].strip().endswith("H"))


if __name__ == "__main__":
    unittest.main()
