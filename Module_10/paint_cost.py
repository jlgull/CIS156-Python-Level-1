#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: paint_cost.py
#

# Import all required options
#
# Import system and name from os
from os import system, name

# End of import section

"""
Ch 10 Programming Assignment, Part A

Create a program called paint_cost.py that prompts the user to input the height of a wall (in feet),
    the width of the wall (in feet), and the cost of the paint used to cover it.
    Output the area of the wall (height x width) and the cost per square foot (cost / area).

Use try and at least two except statements to handle issues that arise if the user does not input numbers or
    enters zero as the area, outputting a relevant message for each issue.

"""

"""

Variable List

Since there are no arrays in Python, so I used a list. Here is information about the (array) List.
List info:


String variables:
    In main program:
        do_again    -   Used in the control of looping the program again.

    In function:
        name    -   In the clear function, finds the type of OS being used.
        system  -   In the clear function, holds the appropriate OS clear command.  
        
        label1          -   Used in dimensional function, to define data being gathered.
        units           -   Used in dimensional function, to define data being gathered.
        entered_data    -   Used in dimensional function, to hold the value entered.
        lower_limit     -   Used in dimensional function for comparison, while checking the data entry.
                  
Floating point numbers:
    In main program:
        wall_width  -   The width of the wall to be painted.
        wall_height -   The height of the wall to be painted.
        wall_area   -   The area of the wall, base on wall_width & wall_height.
  
    In function:

Integers numbers: 
    In main program:
      
    In function:
   
"""

# Function definition section of the program.


def clear():
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is "posix")
    else:
        _ = system("clear")


def get_data(label1, units):
    # Function to request a wall dimension in the units requested,
    # return the value and test for validity.
    # label1    - which dimension (width or height) of wall.
    # units     - the units being requested, feet or inches.
    while True:

        # Setup to request data and convert it to a floating point number,
        #   also prepare for invalid data type.
        try:
            entered_data = float(input(f"Enter {label1} of the wall in {units}: "))
        except ValueError:
            print("Only numbers are allowed.")
            continue

        # Setup to validate that the number is in a valid range.
        try:
            # Use a ternary to set the lower_limit variable.
            lower_limit = 0 if units == "inches" else 1

            # Test that the data is above the lower_limit set above.
            if entered_data < lower_limit:
                raise ValueError(f"Entry for {units} was {entered_data}, which is less than {lower_limit}.")
        except ValueError as error_info:
            print(error_info)
            continue
        break
    # Call a function to test entered data.
    return entered_data


# End of Function definition section.

# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.

    # Create a program called paint_cost.py that prompts the user to input the height of a wall (in feet),
    #   the width of the wall (in feet), and the cost of the paint used to cover it.
    # Prior to starting the program, clear the screen.
    #   If the program is rerun, this will clear the screen as well.
    clear()

    # Print statement to describe the program and expected input data.
    print("\nThis program will ask for the dimensions of a wall in feet and inches.\n"
          "  Then you will be asked for the cost of the paint used to paint the wall.\n"
          "  The output of the program will be the wall dimensions, the wall area, the paint cost\n"
          "    and the cost per square foot for the completed job.")

    # Print a blank line, prior to gathering data.
    print()

    # Call the function (get_data) to gather the rooms dimensions.
    wall_width = get_data("width", "feet") + get_data("width", "inches") / 12
    wall_height = get_data("height", "feet") + get_data("height", "inches") / 12

    # Calculate the wall area.
    wall_area = wall_width * wall_height

    # Get the paint cost for the wall that was painted.
    # Test for valid entry as well.
    while True:
        try:
            paint_cost = float(input("\nEnter the cost of the paint used. For a cost of $3.25, enter 3.25: "))
        except ValueError:
            print("Only numbers are allowed.")
            continue
        try:

            # Test that the data is above the lower_limit set above.
            if paint_cost < 0:
                raise ValueError(f"Entry for paint was less than $0.00.")
        except ValueError as error_feedback:
            print(error_feedback)
            continue
        break

    # Output the area of the wall (height x width) and the cost per square foot (cost / area).
    # Here is the printed output of program.
    print(f"\nThe wall is {wall_width:.2f} feet wide and {wall_height:.2f} feet tall.")
    print(f"The total wall area is {wall_area:.2f} Square feet.")
    print(f"Based on the paint cost of ${paint_cost:.2f}, the cost per Square Foot is $", end="")
    print(f"{paint_cost / wall_area:.2f}.")

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to calculate the the cost of another wall? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input()
        do_again = do_again.upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
