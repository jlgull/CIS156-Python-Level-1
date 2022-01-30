#! / bin / python3
#
# Author: Jonathan Heard
# Work for CIS156, Spring 2022, based on zyBook, CIS156: Python Programming: Level 1
#
# This is a sample Python script, built to follow along with introductory video.

""" Create a program to prompt user for a name and store it in a variable
    The request an age for the user and save it in a variable. """

""" variable list,
    name: for user name
    age: for user age """

first_name = input('Please enter your first name: ')
age = int(input('Please enter your age: '))

# Print the users name

print('\nHello', first_name, ', it is great to meet you!')

# Calculate the users age in 10 years and include it in a message.

print('\tDid you realize that you will be,', age + 10, ', in 10 years?')