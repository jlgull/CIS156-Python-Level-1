#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: shopping_cart.py
#

#
# Import all required options
#
# Import system and name from os
from os import system, name

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
    shopping_cart   - The list of items in the shopping cart.

String variables:
    In main program:
        do_again    -   Flag to control the repeating of the program.
        entered_item_name   - The name of the item put in the shopping cart.

        item_list = ItemToPurchase(entered_item_name, entered_item_price, entered_item_quantity )
    In function:
                  
Floating point numbers:
    In main program:
        entered_item_price = The price of the item placed in the shopping cart.

    In function:

Integers numbers: 
    In main program:
        entered_item_quantity = The quantity of items placed in the cart.
      
    In function:
   
"""

#
# Function definition section of the program
#


def clear():
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.


    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# End of function definitions

# Main body of the program.

# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    """

    Class definition section of the program
    
    (1) Create the ItemToPurchase class with the following specifications:
    
        Attributes
            item_name (string)
            item_price (float)
            item_quantity (int)
        Default constructor
            Initializes item's name = "none", item's price = 0, item's quantity = 0
        Method
            print_item_cost()
        
        Example of print_item_cost 
            Bottled Water 10 @ $1.25 = $12.5
    """

    # Clear the screen on the first run or any repeated use of the program
    clear()

    # Create the new class.
    class ItemToPurchase:

        # Initial items names and values.
        def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
            self.item_name = item_name
            self.item_price = item_price
            self.item_quantity = item_quantity

        # Create print method
        def print_item_cost(self):
            return (f"{self.item_name} {self.item_quantity} @ "
                    f"${self.item_price:.2f} = ${self.item_price * self.item_quantity:.2f} ")

    # This was created to test the development of the class.
    # item1 = ItemToPurchase("Chocolate Chips", 3.5, 1)

    """

    (2) In the main section of your code (not in the class definition), prompt the user for two items and create
        two objects of the ItemToPurchase class.
    
        Example of a program run after step 2:
    
            Item 1
            Enter the item name:
            Chocolate Chips
            Enter the item price:
            3.50
            Enter the item quantity:
            1
    """

    # This is the main body of the program, as required for section (2). This portion will query the user for
    #   either 2 items, as required for CIS156 or it will be an unlimited list, that goes on until there is
    #   no entry.

    # Initialize the empty shopping cart.
    shopping_cart = []

    print("This is the entry portion, for the shopping cart.\n"
          "For each record enter the requested information.\n")

    for i in range(2):
        print(f"Item {i+1}")
        entered_item_name = input("Enter the item name:\n").title()
        entered_item_price = float(input("Enter the item price, for example 1.25 for $1.25:\n"))
        entered_item_quantity = int(input("Enter the item quantity:\n"))
        item_list = ItemToPurchase(entered_item_name, entered_item_price, entered_item_quantity)
        shopping_cart.append(item_list)
        print()   # This print statement is just for spacing between multiple entries.



    """
    (3) Add the costs of the two items together and output the total cost.
    
    Example of output from additional code in step 3:
    
        TOTAL COST
        Chocolate Chips 1 @ $3.5 = $3
        Bottled Water 10 @ $1.25 = $12.5
        
        Total: $15.5

    """

    total_cost = 0
    print("Your shopping cart hold 2 items, here are the details.")
    print("TOTAL COST")
    for i in range(2):
        print(shopping_cart[i].print_item_cost())
        total_cost += shopping_cart[i].item_price * shopping_cart[i].item_quantity
    print(f"\nTotal: ${total_cost:.2f}")

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to revisit the shopping cart? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
