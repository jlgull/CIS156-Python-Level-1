#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: shipping_price.py
#
"""

Ch 6 Programming Assignment, Part B

Create a program called shipping_price.py that calculates the shipping price for a purchase.
Use a prompt to get (from the user) the number of items and the total weight of the package (in pounds).
Then pass that data to a user-defined function that accepts both values as parameters and
    returns (not outputs) a shipping price based on the following guidelines:

    Less than 3 items and less than one pound: $5.00 shipping charge.
    Less than 3 items and one pound or over: $7.50 shipping charge.
    3 to 5 items and less than two pounds: $8.50 shipping charge.
    Anything else: $10.00 shipping charge.

Display this returned value for the user.

"""

"""
Variable List

String variables:
    do_again  -   will collect the response for running the program again

Floating point numbers:
In main program (shipping_price.py):
    total_weight    -   weight of items being shipped.
    total_ship_cost -   shipping cost calculated in function 

In function (calc_shipping_cost):
    weight      -   total_weight passed to the function
    cost        -   cost determined in function and returned

Integers numbers: 
In main program (shipping_price.py):
    items_count     -   the number of items to be shipped

In function (calc_shipping_cost):
    count       -   items_count, passed to the function 


"""

"""
# Define the function to calculate shipping costs,
#   based on the number of items being shipped
#   and the total weight of all the items being shipped.

Then pass that data to a user-defined function that accepts both values as parameters and
    returns (not outputs) a shipping price based on the following guidelines:

    Less than 3 items and less than one pound: $5.00 shipping charge.
    Less than 3 items and one pound or over: $7.50 shipping charge.
    3 to 5 items and less than two pounds: $8.50 shipping charge.
    Anything else: $10.00 shipping charge.

"""


def calc_cost(count, weight):
    # If the count is less than 3.
    if count < 3:
        cost = 7.5 if weight >= 1 else 5.0

    # If the count is 3 to 5 items and less than two pounds.
    elif (3 <= count <= 5) and weight < 2.0:
        cost = 8.5

    # If anything else.
    else:
        cost = 10

    # Return the shipping cost.
    return cost


# End of Function definition

# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main program
    # Use a prompt to get (from the user) the number of items
    # and the total weight of the package (in pounds).
    # Using while and try to ensure that the correct data type is entered

    # Collect the number of items be shipped, it must be an integer.
    while True:
        try:
            items_count = int(input("\nPlease enter the number of items being shipped. "))
        except:
            print("Your entry was not an integer, please enter a number.")
        else:
            break

    # Collect the weight of items be shipped, it must be a floating point number.
    while True:
        try:
            total_weight = float(input("Enter the total weight in pounds, as a decimal value. "))
        except:
            print("Your entry was not a floating point number, try again.")
        else:
            break

    # Call the function, to calculate the total shipping cost.
    total_ship_cost = calc_cost(items_count, total_weight)

    # Display this returned value for the user.
    # Print statement to print the returned value.
    # Print a blank line between the data entered and the results.
    print("\n")

    # If there is only one item, use the singular form of item.
    if items_count == 1:
        print(f"To ship your {items_count} item,", end="")
    else:
        print(f"To ship your {items_count} items", end="")

    # Print the remainder of the message.
    print(f" which weights {total_weight:.2f} pounds.")
    print(f"Your shipping charge is ${total_ship_cost:.2f}.")

    # The following code as copied from the sum_loop program.
    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to calculate your shipping charges again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input()
        do_again = do_again.upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
