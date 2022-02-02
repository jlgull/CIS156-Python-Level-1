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

Sample Output:


"""


""" Create a program to prompt user for a name and store it in a variable
    The request an age for the user and save it in a variable. """

""" variable list,
    first_name: for user name
    age: for user age
    new_age for age 10 years in the future """

first_name = input('Please enter your first name: ')
age = int(input('Please enter your age: '))

# Print the users name

print('\nHello', first_name, ', it is great to meet you!')

# Calculate a new varialbel with the users age in 10 years and include it in a message.

new_age = age + 10

print('\tDid you realize that you will be', new_age, 'years old, in 10 years?')