#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: math_module_1st_try.py
#
"""
Generic shell for the CIS156 programs

Ch XX Programming Assignment, Part ??

Copy instructions from Canvas, change the program name as required.


"""
#
# Import all required options
#
# Import system and name from os
from kennedy_13 import clear, get_data

# import sleep to show output for some time period
from time import sleep

# End of import section


"""

Variable List

Since there are no arrays in Python, so I used a list. Here is information about the (array) List.
List info:


String variables:
    In main program:
        do_again    -   Control value for repeating the program.

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
clear()

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.


    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to run this program again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
