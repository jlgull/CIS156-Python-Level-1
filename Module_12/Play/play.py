#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

#
# Define functions
#

class Subtract:

    def __init__(self, num1, num2):

        self.num1= num1

        self.num2 = num2

    def calculate_diff(self):

        diff = self.num1 - self.num2

        print(diff)


diff1 = Subtract()

# End of program
