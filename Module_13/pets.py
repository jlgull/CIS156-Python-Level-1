#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: pets.py
#
"""
Ch 13 Programming Assignment

Create a program called pets.py that that defines a pet class with at least three general
    attributes (fields) for all pets (for example, name, age, etc) and at least two functions/behaviors
    for all pets (for example, eating). The functions can simply print something.

Next, create two derived classes from the base class that represent specific types of pets.
    For example, one derived class might be a dog. Add at least one attribute/field and at least
    two functions/behaviors specific to that kind of pet.

Finally, demonstrate that both derived classes work by creating at least one instance of each and
    showing off their fields and functions.

Note: In preparation for the Final Project, this assignment leaves room for you to make more
    decisions about the code than previous assignments. Just be sure that your submission demonstrates the key
    concepts from the chapter, as indicated in these directions.

"""
#
# Import all required options
#
# Import system and name from os

from kennedy_13 import clear, get_data
""" This is a module written to contain tools used throughout the main program
        to reduce the duplication of code as the designed moved forward.
        clear() - Performs a screen clear using the OS module and is intended to by Operating System (OS)
                    independent or agnostic.
        get_data    - Is used for all data entry requests. It used try/except to ensure that the data
                        entered is the type expected and it also expects a clarifying question or statement. 
"""


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
