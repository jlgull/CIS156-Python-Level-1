#!/bin/python3
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

# oop/operator.overloading.py
class Weird:
    def __init__(self, s):
        self._s = s
    def __len__(self):
        return len(self._s)
    def __bool__(self):
        return '9' in self._s

weird = Weird('Hello! I am 9 years old!')
print(f"The length of entry was: {len(weird)} characters.")  # 24
print(bool(weird)) # False

weird2 = Weird('Hello! I am 42 years old!')
print(f"The length of entry was: {len(weird2)} characters.") # 25
print(bool(weird2)) # True



# End of program
