#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

from kennedy_13 import clear, get_data


#
# Define functions
#
# Main Menu module for CIS156 Final Project
def menu():

    # Define the menu items.

    while True:

        menu_items = {
                        1:  "2000 Data",
                        2:  "2010 Data",
                        3:  "2020 Data",
                        4:  "Exiting"
                     }

        for i in range(1, len(menu_items)+1):
            print(f"Select item ({i}) for {menu_items[i]}")

        print()

        choice = get_data("i", "Select which year's data you would like to analyze. ")

        if choice > len(menu_items):
            print(f"Your choice, {choice}, is greater than {len(menu_items)}, pick again. \n")
            continue
        return choice





# End of Functions



# This is set up to allow for testing, during development of the
#   menu design in the package.
# Test if this is being used as a script?
if __name__ == "__main__":

    clear(), print()

    choice = menu()

    print(f"You chose: {choice}")

# End of Program
