import unittest
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src/ListCommands")
    )
)

from util import process_commands


class TestListCommands(unittest.TestCase):

    def test_sample(self):
        commands = [
            "insert 0 5",
            "insert 1 10",
            "insert 0 6",
            "print",
            "remove 6",
            "append 9",
            "append 1",
            "sort",
            "print",
            "pop",
            "reverse",
            "print"
        ]

        result = process_commands(commands)

        self.assertEqual(result[0], [6, 5, 10])
        self.assertEqual(result[1], [1, 5, 9, 10])
        self.assertEqual(result[2], [9, 5, 1])


if __name__ == "__main__":
    unittest.main()
