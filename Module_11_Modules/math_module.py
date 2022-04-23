#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: math_module_1st_try.py
#
"""
Generic shell for the CIS156 programs

Ch 11 Programming Assignment, Part B

Create a program called math_module_1st_try.py that uses the math module (https://docs.python.org/3.5/library/math.html
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


from kennedy_13 import clear


from math import factorial, pow


# Explain the 2 math modules imported.

"""  math.factorial(x)
        Return x factorial as an integer. Raises ValueError if x is not integral or is negative.  """

"""  math.pow(x, y)
        Return x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible.
         In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN (Not a Number). 
         If both x and y are finite, x is negative, and y is not an integer then pow(x, y) is undefined,
            and raises ValueError.

        Unlike the built-in ** operator, math.pow() converts both its arguments to type float. 
         Use ** or the built-in pow() function for computing exact integer powers.  """

# End of import section

"""

Variable List

Since there are no arrays in Python, so I used a list. Here is information about the (array) List.
List info:


String variables:
    In main program:
        do_again    - Control for repeating the program.

    In function:
                  
Floating point numbers:
    In main program:
        float_entry     - The value returned to the main program.
  
    In function:
        entered_data    - The entered data, converted to a floating point number.
Integers numbers: 
    In main program:
        int_entry       - The absolute value of floating point number converted to an integer. 
      
    In function:

"""

# Function definition section of the program


def get_data():
    # Function to request a numerical data, test for validity and
    # return the entered data.
    while True:

        # Setup to request data and convert it to a floating point number,
        #   also prepare for invalid data type.
        try:
            entered_data = float(input(f"Enter your number: "))
        except ValueError:
            print(f"Only numbers are allowed.")
            continue
        break

    return entered_data

# End of function definitions


# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.

    # Clear the screen, prior to running the program.
    clear()

    # Explain the program and the expected input and output.
    print(f"This program will ask for a single number and return the number raised to the 3rd power\n"
          f"  and the factorial of the number as well.")
    print(f"Any number, floating point or integer is acceptable. In addition if the number is a\n"
          f"  negative floating point number, it will be converted to its absolute integer value\n"
          f"  before being passed to the factorial module.")

    # Prompt the user to enter a number.
    float_entry = get_data()

    # Entry to test the value, removed for final product.
    #print(type(float_entry))

    # Convert floating point number to a positive integer.
    int_entry = int(abs(float_entry))

    # Entry to test the value, removed for final product.
    #print(type(int_entry))

    # Calculate and output the factorial of the entered number using a function from the math module.
    #         For example, the factorial of 4 is 24.
    print(f"\nThe factorial of {int_entry} is {factorial(int_entry):,}.")

    # Calculate and output the value of the entered number raised to the power of 3 using a function from the
    #         math module. For example, 4 raised to the power of 3 is 64.
    print(f"\nYour number, {float_entry}, raised to the 3rd power is ", end='')
    print(f"{pow(float_entry, 3):,}.")

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
