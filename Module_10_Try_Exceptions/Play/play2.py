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

entered_feet_inches = input("Enter the wall width in feet and inches. Put a comma between the feet and inches: ")

print(len(entered_feet_inches))

entered_feet_inches = entered_feet_inches.split(",")

width_feet = float(entered_feet_inches[0]) + float(entered_feet_inches[1]) / 12

print(width_feet)


# End of program
