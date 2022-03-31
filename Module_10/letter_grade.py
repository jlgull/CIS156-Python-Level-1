#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: letter_grade.py
#

# Import all required options
#
# Import system and name from os
from os import system, name

# End of import section


"""
Ch 10 Programming Assignment, Part B

Create a program called letter_grade.py that asks the user to input their current grade percentage and
    then outputs the corresponding letter grade (A through F).

Within a try-except structure raise (not just catch) two different exceptions: one if the user inputs a grade
    of less than zero and a different exception if the user inputs a grade greater than 100.
    Be sure to also handle input that is not a number.

Note that you can use a ValueError (as described in zyBooks 10.3) and do not need to create a
    custom exception (as described in 10.6).

"""

"""

Variable List

Since there are no arrays in Python, so I used a list. Here is information about the (array) List.
List info:


String variables:
    In main program:
        letter_grade    -   The Letter grade determined by the program

    In function:
        name    -   In the clear function, finds the type of OS being used.
        system  -   In the clear function, holds the appropriate OS clear command.  
    
                  
Floating point numbers:
    In main program:
        grade   -   The numerical value entered.
        
    In function:

Integers numbers: 
    In main program:
      
    In function:
   
"""

# Function definition section of the program
#


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


#
# End of function definition section
#

# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.

    """
    Create a program called letter_grade.py that asks the user to input their current grade percentage and
    then outputs the corresponding letter grade (A through F).

    Found the letter grade information in the CIS156 Syllabus, page 3 of 4.
        90% - 100% = A
        80% - 89% = B
        70% - 79% = C
        60% - 69% = D
        0% - 59% = F
    """

    # Clear the screen prior to each run.
    clear()

    # Print information about the program.
    print("\nWelcome the the Letter grade derivation program.\n"
          "\nPlease enter your current grade percentage,\n"
          " and the program will return your your Letter grade.")

    # Request the numerical grade from the user.
    # Validate that the data entered is a number and
    #   between the limits of 0 and 100.
    while True:

        # Test the data entered is a floating point number.
        try:
            grade = float(input("\nEnter current grade percentage, between 0 and 100:  "))
        except ValueError:
            print("Only numbers are allowed.")
            continue

        # Test that the grade is between 0 and 100.
        try:
            if grade < 0 or grade > 100:
                raise ValueError(f"Your entered grade, {grade:.2f}, in not between 0 and 100.")
        except ValueError as error_feedback:
            print(error_feedback)
            continue
        break

    # Determine the letter grade, with ternary based single in-line if statement.
    letter_grade = "A" if grade >= 90.0 else "B" if grade >= 80.0 else "C" if grade >= 70.0 else "D" \
        if grade >= 60.0 else "F"

    # Print out the number grade entered and the letter grade equivalence.
    print(f"\nThe current grade percentage entered was {grade:.2f},", end=""
          f" which equates to a Letter grade of \"{letter_grade}\".\n")

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to determine another Letter grade? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
