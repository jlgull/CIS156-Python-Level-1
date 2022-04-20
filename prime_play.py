#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
from kennedy_13 import clear, get_data
""" This is a module written to contain tools used throughout the main program
        to reduce the duplication of code as the designed moved forward.
        clear() - Performs a screen clear using the OS module and is intended to by Operating System (OS)
                    independent or agnostic.
        get_data    - Is used for all data entry requests. It used try/except to ensure that the data
                        entered is the type expected and it also expects a clarifying question or statement. 
"""

#
# Define functions
#


# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    prime_numbers = list()
    not_prime_number = list()

    prime_numbers.append(1)
    prime_numbers.append(2)

    # Main body of the program.

    clear()

    print(f"\nThis program will find all the prime numbers between 1 and the number you enter.")

    end_number = get_data("i", "Enter your number now: ")

    for outside_loop in range(3, end_number+1, 2):
        for inside_loop in range(3, outside_loop+1, 2):
            if outside_loop % inside_loop == 0 and inside_loop in prime_numbers:
                not_prime_number.append(outside_loop)
                break
            if outside_loop % inside_loop == 0 and inside_loop not in prime_numbers:
                prime_numbers.append(outside_loop)

    print(f"Between 1 and {end_number} there are {len(prime_numbers)} Prime numbers.\n"
          f"Here is your list:\n{prime_numbers}")

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to run this again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of Program
