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

from time import perf_counter, perf_counter_ns

from dateutil.relativedelta import *

#
# Define functions
#



birth_day = date(int(input("Enter birth year: ")),int(input("Enter birth month: ")),
                 int(input("Enter birth day: ")))

today = date.today()

print(birth_day, today)

age = relativedelta(today, birth_day)


print(age.years, age.months, age.days)

# More examples at: https://www.plus2net.com/python/date-relativedelta.php

print(f"Current Age: {age.years} years, {age.months} months and {age.days} days.")

print(dir(relativedelta))


# End of program

