#! / bin / python3
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


from clear_screen import clear


from math import factorial, pow


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

    In function:
                  
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
      
    In function:

"""

# Function definition section of the program


def get_data(data_type, allow_neg):
    # Function to request a numerical data, test for validity and
    # return the entered data.
    # data_type     - what data type, integer or floating point.
    # allow_neg     - Allow negative numbers, Yes or No.
    while True:

        # Setup to request data and convert it to a floating point number,
        #   also prepare for invalid data type.
        try:
            if data_type == "Float":
                entered_data = float(input(f"Enter your number: "))
            else:
                entered_data = int(input(f"Enter your number: "))
        except ValueError:
            print(f"Only {data_type} numbers are allowed.")
            continue

        # Setup to validate that the number is in a valid range.

            # Test that the data is above the lower_limit set above.
        if allow_neg == "No" and entered_data < 0:
            print(f"Entered number must be greater than 0.")
            continue
        break
    # Call a function to test entered data.
    return entered_data

# End of function definitions


# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.

    # Clear the screen, prior to running the program.
    clear()

    # Ask if the user which function, factorial or pow, they would like to run.
    # Also, validate for the correct response.
    while True:
        print("\nWhich function would you like to run.\n"
              "Enter \"F\" for Factorial or \"P\" for Power.", end=" ")
        function_request = input().upper()
        if function_request != "F" and function_request != "P":
            print("The only valid entries are either an \"F\" or a \"P\".")
        elif function_request == "F":
            """ Calculate and output the factorial of the entered number using a function from the math module.
                    For example, the factorial of 4 is 24. """
            print("\nEnter the number you would like to calculate the factorial of.")
            print("The program will then calculate the factorial of the number 1 and then up to the number "
                  "you enter."
                  "\nEnter the number, integer, you would like as the highest factorial to be calculated.")
            print("   There is no limit to the number that you can enter;\n"
                  "      but be aware that any number larger than 100 will\n"
                  "      be wider than your screen, take some time, and return a lot of 0's.")
            number_entry = get_data("Integer", "No")

            # Loop from 1 to the number the user entered.
            for i in range(1, number_entry+1):

                # Print the results of all the factorials calculated.
                print(f"\nThe factorial of {i} is {factorial(i):,}.")

            break
        else:
            #if function_request == "P":
            """ Calculate and output the value of the entered number raised to the power of 3 using a 
                    function from the math module. For example, 4 raised to the power of 3 is 64. """
            print("\nThe function \"pow\" is being used to find your number raised to the 3rd power.\n"
                  "   Your number can be either an integer or a floating point number.")

            number_entry = get_data("Float", "Yes")

            print(f"\nYour number, {number_entry}, raised to the 3rd power is ", end='')
            print(f"{pow(number_entry, 3):,}.")
            break

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
