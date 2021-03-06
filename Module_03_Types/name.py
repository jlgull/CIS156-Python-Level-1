#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: name.py
#
# Ch 3 Programming Assignment, Part A

"""
Create a program named name.py that prompts the user to input their first name and stores it in a variable.
    Then prompt the user for their last name,
    and store that in a second variable.
    Use their input to do each of the following:

    Create a variable with their full name (first and last), and then print it
    Output the length of the full name
    Output the user's initials (first letter in the first name and first letter in the last name)
    Output the fourth letter in the first name
"""


""" variable list,
    first_name: for the user's first name
    last_name:  for the user's last name
    full_name:  for the user's full name 
"""

# Prompts the user to input their first name and store it in a variable.

first_name = input('Please enter your first name:\n')

# Prompt the user for their last name and store it in a variable.

print(first_name , ", please enter your last name:")
last_name = input()

# Create a variable with their full name (first and last), and then print it

full_name = first_name + " " + last_name

print("\nHello", full_name, ", it's great to meet you!")

# Output the length of the full name

print("\n\tThe length of your full name is:", len(full_name), "characters long.")

# Output the user's initials (first letter in the first name and first letter in the last name)

print("\n\tYour initials are:", first_name[0] + last_name[0])

# Output the fourth letter in the first name

if len(first_name) < 4:
    print("\n", first_name, ", there is no 4th letter in your first name.")
else:
    print("\t", first_name, ", the 4th letter in your first name is:", first_name[3])

# End of program
