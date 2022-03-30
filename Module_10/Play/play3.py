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

user_input = ''
while user_input != 'q':
    try:
        weight = float(input('Enter weight (in pounds): '))
        if weight < 0:
            raise ValueError('Invalid weight.')

        print(weight)


    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')
    


user_input = input("Enter any key ('q' to quit): ")




# End of program
