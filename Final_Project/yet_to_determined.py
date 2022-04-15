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

Final Project Programming Assignment

The project must demonstrate ALL of the following skills/concepts:

    The project must be your original work. The majority of the Python used must be your own work;
      any code that is based on (or borrowed from) someone else's work must be clearly identified and
      cited both as code comments and in the documentation page below, including specific URLs if applicable.
      You will not receive credit for completing a tutorial or modifying/adapting code from another programmer
      or source.

    The project should consist of a single Python program/script,
      or up to three separate programs that are all related to one another.

    At least one if-statement (with or without elif and else).

    Creation of a function that accepts at least one parameter/argument. This requirement cannot be met using a
      simple "set" method.

    Creation of a function that returns a value--with that returned value used in a meaningful way.
      This requirement cannot be met using a simple "get" method.
      Note: this may be the same function that accepts a parameter for the previous requirement,
        or it may be a different function.

    Use of a loop in a meaningful way. (For example, a loop that iterates only one time before being
      stopped isn't meaningful. Likewise, a loop that iterates multiple times but does nothing
      useful/significant within the project isn't meaningful.)

    Basic exception handling using try-except structures.

    A completed Project Documentation file: CIS156 Final Project Documentation.docx
      In addition to providing basic information, this file is used to ensure that your instructor does
      not miss anything when grading--so it is very important to complete this thoroughly and carefully.

Your project must demonstrate AT LEAST ONE of the following elective skills/concepts:

    A user-defined class (as covered in module 9) used in a meaningful way. The use of inheritance is not required.

    A list or dictionary structure used in a meaningful way

    -or-

    Reading and/or writing files, used in a meaningful way.

"""
#
# Import all required options
#
# Import system and name from os
from kennedy_13 import clear


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
