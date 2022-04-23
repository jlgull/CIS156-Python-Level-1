#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

import unittest

# Define functions
#


def evens(numbers):
    """Return the even values in numbers"""
    return [i for i in numbers if (i % 2 == 0)]


def odds(numbers):
    """Return the odd values in numbers"""
    return [i for i in numbers if (i % 2 == 1)]


class TestNumbers(unittest.TestCase):
    test_nums = [1, 3, 5, 6, 8, 2, 1]

    def test_evens(self):
        self.assertEqual(evens(), 6, 8, 2)

    def test_odds(self):
        self.assertEqual(odds(), 1, 3, 5, 1)


if __name__ == "__main__":
    unittest.main()


# End of program
