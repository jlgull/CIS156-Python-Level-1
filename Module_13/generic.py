#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: yet_to_determined.py
#
"""
Generic shell for the CIS156 programs

Ch 13 Programming Assignment, Part ??

Copy instructions from Canvas, change the program name as required.


"""
#
# Import all required options
#
# Import system and name from os
from clear_screen import clear


# End of import section


"""

Variable List

Since there are no arrays in Python, so I used a list. Here is information about the (array) List.
List info:


String variables:
    In main program:

    In function:
                  
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
      
    In function:
   
"""

#
# Function definition section of the program
#


# End of function definitions



# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.

    clear()

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to calculate the sum of your bills again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
