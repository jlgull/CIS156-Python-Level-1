#! / bin / python3
#
# Author: Jonathan Heard
# Work for CIS156, Spring 2022, based on zyBook, CIS156: Python Programming: Level 1
# Program name: family.py
#
# Ch 3 Programming Assignment, Part B

"""
Create a program named family.py with a dictionary of names and ages for a family of at least four people;
    this may be your family or a fictional family (such as the Simpsons).
    Print out the dictionary.
    Then, print just the age of the 2nd person in the dictionary.
    Finally, add an entry for "Tim" with the age 46, and print the full dictionary again.

"""


""" 
Create a program named family.py with a dictionary of names and ages for a family of at least four people;
    this may be your family or a fictional family (such as the Simpsons).
    
    variable list,
    family_dict - Dictionary to hold family names and ages
    age: for user age
    new_age for age 10 years in the future 

"""

# Create empty dictionary

# family_dict = dict()

# Put fictional family in the dictionary, include name and age

family_dict = {
    "Samson": 44,
    "Jason": 42,
    "Collin": 14,
    "Lucas": 11
    }

# Print out the dictionary.

print("\n", family_dict)

# Then, print just the age of the 2nd person in the dictionary.

print("\nJason is", family_dict["Jason"], "years old.")

# Add an entry for "Tim" with the age 46, and print the full dictionary again.

family_dict["Tim"] = 46

print("\n", family_dict)
