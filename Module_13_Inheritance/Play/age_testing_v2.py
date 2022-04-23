#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
from datetime import date, timedelta

#
# Define functions
#
#year = int(input("Enter birth year: "))
#month = int(input("Enter birth month: "))
#day = int(input("Enter birth day: "))

born = date(int(input("Enter birth year: ")),int(input("Enter birth month: ")),
                 int(input("Enter birth day: ")))

today = date.today()

age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

print(age)

# End of program
