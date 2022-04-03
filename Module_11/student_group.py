#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: student_group.py
#

"""

Ch 11 Programming Assignment, Part A

Create a program called student_group.py that the random module (https://docs.python.org/3.5/library/random.html
(Links to an external site.)) to create a list of random students to work together on a group project, as follows:

    Create a list of at least 10 student names.
    Prompt the user to input how many students should be in the group.
    Generate a random number appropriate to the number of names in the list
    Use the random number to retrieve and print the corresponding name from the list.
    Repeat until you have output the correct number of students, as input by the user.

Note: This program will have a flaw--the same student could be chosen multiple times.
    Although you can solve this issue if you want, you are not required to address it for the assignment.

Sample Output:

    Input the number of students in the group: 5
    The group is:
    Jane
    Jesus
    Derek
    Isabella
    Mai

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



    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to run the program again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
