#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
from kennedy_13 import clear

from math import pi, pow

#
# Define functions
#

# Start of program

clear()

# Read file

address = open("address.txt")

lines = address.readlines()

print(lines)

for line in lines:
    print(line)




# End of program
