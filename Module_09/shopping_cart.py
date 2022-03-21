#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: shopping_cart.py
#
"""
Generic shell for the CIS156 programs

Ch 09 Programming Assignment

Create a program called shopping_cart.py that uses a class and objects to track a couple of items for purchase
    from an online store. There are three steps/sections to this program:

(1) Create the ItemToPurchase class with the following specifications:

    Attributes
        item_name (string)
        item_price (float)
        item_quantity (int)
    Default constructor
        Initializes item's name = "none", item's price = 0, item's quantity = 0
    Method
        print_item_cost()

(2) In the main section of your code (not in the class definition), prompt the user for two items and create
    two objects of the ItemToPurchase class.

(3) Add the costs of the two items together and output the total cost.

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

"""

Function definition section of the program

"""

"""

Class definition section of the program

"""

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
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
