#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: paint_cost.py
#
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

    In function:
        name    -   In the clear function, finds the type of OS being used.
        system  -   In the clear function, holds the appropriate OS clear command.  
        label1          -   Used in both dimensional functions, to define data being gathered.
        entered_feet    -   Used in the feet dimensional function, to hold the value in feet.
        entered_inches  -   Used in the inches dimensional function, to hold the value in inches.
                  
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

#
# Import all required options
#
# Import system and name from os
from os import system, name

# End of import section


# Function definition section of the program.


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


def get_feet(label1):
    # Function to request a wall dimension in feet and
    # return the value.
    # label1    - which dimension   (width or height) of wall.
    entered_feet = input(f"\nEnter {label1} of the wall in feet: ")

    # Error message if the entry is a string or text.
    if entered_feet.isalpha():
        raise ValueError('Only numbers are allowed.')
    entered_feet = float(entered_feet)

    # Error message if the entry is less than 0.
    if entered_feet < 0:
        raise ValueError('Entry for feet was less than 0.')
    return entered_feet


def get_partial_feet(label1):
    # Function to request the additional wall dimension in inches and
    # return it in partial feet.
    # label1    - which dimension (width or height) of wall.
    entered_inches = input(f"Enter{label1} of the wall in inches: ")

    # Error message if the entry is a string or text.
    if entered_inches.isalpha():
        raise ValueError('Only numbers are allowed.')
    entered_inches = float(entered_inches)

    # Error message if the entry is less than 0.
    if entered_inches < 0:
        raise ValueError('Entry for inches was less than 0.')
    return entered_inches / 12


# End of Function definition section.

# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.

    # Create a program called paint_cost.py that prompts the user to input the height of a wall (in feet),
    #   the width of the wall (in feet), and the cost of the paint used to cover it.
    # Prior to starting the program, clear the screen.
    # If the program is rerun, then clear the screen as well.
    clear()

    # Print statement to describe the program and expected input data.
    print("\nThis program will ask for the dimensions of a wall in feet and inches.\n"
          "  Then you will be asked for the cost of the paint used to paint the wall.\n"
          "  The output of the program will be the wall dimensions, the wall area, the paint cost\n"
          "    and the cost per square foot for the completed job.")

    try:

        # Call the 2 functions (get_feet) and (get_partial_feet) to gather
        # the rooms dimensions.
        wall_width = get_feet("width") + get_partial_feet("width")
        wall_height = get_feet("height") + get_partial_feet("height")


        # Calculate the wall area
        wall_area = wall_width * wall_height

        # Get the paint cost for the wall that was painted.
        paint_cost = float(input("\nEnter the cost of the paint used. For a cost of $3.25, enter 3.25: "))

        # Output the area of the wall (height x width) and the cost per square foot (cost / area).
        # Here is the printed output of program.
        print(f"\nThe wall is {wall_width:.2f} feet wide and {wall_height:.2f} feet tall.")
        print(f"The total wall area is {wall_area:.2f} Square feet.")
        print(f"Based on the paint cost of ${paint_cost:.2f}, the cost per Square Foot is $", end="")
        print(f"{paint_cost / wall_area:.2f}.")


    except ValueError as excpt:
        print(excpt)
        print('Could not calculate painting costs from the information supplied.\n')

    except ValueError:
        print("Only numbers are allowed, no text entries.")


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
