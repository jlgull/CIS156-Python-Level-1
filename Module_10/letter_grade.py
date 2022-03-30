#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: letter_grade.py
#
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

    In function:
                  
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
      
    In function:
   
"""

# Function definition section of the program
#
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
