#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
#
# Program name: menu_builder.py
#
#This module is used to build the menu for the selection of the data to be analyzed.
#


#
# Import all required options.
#

from kennedy_13 import clear, get_data
# This is a module containing the following tools, written to reduce the duplication of code as the designed
#       moved forward.
#clear() - Performs a screen clear using the OS module and is intended to by Operating System (OS)
#           independent or agnostic.
#get_data    - Is used for all data entry requests. It uses try/except to ensure that the data
#           entered is the correct type, it also expects a clarifying question or statement.


#
# End of Import section.

"""

Variable List

Dictionary info:
    menu_items      -   Dictionary to hold menu items.

Integers numbers: 
    In main program:
        picked_choice   - Item picked from the menu list.
        year_choice     - The number being returned to the calling program.

"""


# Define functions
#
# Main Menu module for CIS156 Final Project
def menu():

    while True:

        # Define the menu items.
        menu_items = {
                        1:  "2000 Data",
                        2:  "2010 Data",
                        3:  "2020 Data",
                        4:  "Ending the program"
                     }

        # Print out the Menu items.
        for i in range(1, len(menu_items)+1):
            print(f"Select ({i}) for {menu_items[i]}")

        # Print a blank line prior to gathering the choice selection.
        print()

        # Gather the selection for which data set to analyze.
        picked_choice = get_data("i", "Select which year's data you would like to analyze. ")

        # Validate that the choice is within the limits of the options.
        if picked_choice > len(menu_items):
            print(f"Your choice, {picked_choice}, is greater than the {len(menu_items)} options available,"
                  f" please pick again. \n")
            continue
        if picked_choice == 1:
            year_choice = 2000
        elif picked_choice == 2:
            year_choice = 2010
        elif picked_choice == 3:
            year_choice = 2020
        else:
            year_choice = False
        return year_choice

#
# End of Functions
#


# This is set up to allow for testing, during development of the
#   menu design in the package.
# Test if this is being used as a script?
if __name__ == "__main__":

    # If testing this module, clear screen and print a blank line.
    clear(), print()

    # Call the menu function to test it.
    choice = menu()

    # Print results, as part of the test.
    print(f"You chose: {choice}")

# End of Program
