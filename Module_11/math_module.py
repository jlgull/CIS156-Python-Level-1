#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: math_module.py
#
"""
Generic shell for the CIS156 programs

Ch 11 Programming Assignment, Part B


Create a program called math_module.py that uses the math module (https://docs.python.org/3.5/library/math.html
    (Links to an external site.)) to do the following:

    Prompt the user to enter a number.
    Calculate and output the factorial of the entered number using a function from the math module.
        For example, the factorial of 4 is 24.
    Calculate and output the value of the entered number raised to the power of 3 using a function from the
        math module. For example, 4 raised to the power of 3 is 64.

Hint: You may find the w3schools (Links to an external site.) math module reference helpful in solving Part B.

"""

#
# Import all required options
#
# Import system and name from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# End of import section



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




# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.


    # The following code as copied from the sum_loop program.
    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to run the program again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program.
