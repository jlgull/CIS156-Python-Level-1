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



#birth_day = date(int(input("Enter birth year: ")),int(input("Enter birth month: ")),
                 # int(input("Enter birth day: ")))

birth_day = date(int(input("Enter birth year: ")),1,1)

print(birth_day)
today = date.today()
# age = today.year - birth_day.year  # -
# ((today.month, today.day) <
age_in_years = today.year - birth_day.year
age_in_months = today.month - birth_day.month
if age_in_months < 0:
    age_in_years -= 1
    age_in_months = age_in_months + 12
age_in_days = today.day - birth_day.day
if age_in_days < 0:
    age_in_months -= 1
    age_in_days = age_in_days + 31

print(age_in_years, age_in_months, age_in_days)

print(timedelta(today,birth_day))

# End of program
