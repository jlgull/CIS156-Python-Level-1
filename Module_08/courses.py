#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: generic.py
#
"""
Generic shell for the CIS156 programs

Ch 8 Programming Assignment, Part B

Create a program called courses.py that has a dictionary with 7 course names
    (for example: CIS105, ENG101, etc), along with the name of each associated instructor.
Prompt the user for the name of a course to look up, or the word "quit" to exit.
After the user types in a course, it should look up and print that course's instructor.

The program should repeat this until the user enters "quit" at the prompt.

Note: The program does NOT need to gracefully handle the error that may occur if the course
    is not found in the dictionary; for now, your program only needs to work when a course is entered correctly.

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
        do_again = input()
        do_again = do_again.upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
