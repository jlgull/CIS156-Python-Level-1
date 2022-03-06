#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: generic.py
#
"""
Generic shell for the CIS156 programs

Ch 8 Programming Assignment, Part A

Create a program called grocery_list.py that allows the user to input a list of items to buy at the
    supermarket. It should begin by asking the user to input the number of items to add to the list.
    Then, it should use a loop to prompt the user to input that many items, storing each in the list.

After the items have been entered, it should output the full list.

"""

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

# Function definition section of the program



# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.


    # The following code as copied from the sum_loop program.
    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to calculate the sum of your bills again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input()
        do_again = do_again.upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
