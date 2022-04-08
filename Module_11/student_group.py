#!/usr/bin/env python3
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
# Import clear screen.
from clear_screen import clear

# List of 2000 baby names from the 2020 SSN database.
#   Found as a JSON file and converted to Python lists.
from baby_boy_names import *
from baby_girl_names import *

# From the Random module, import selected tools.

from random import sample, randint

"""  random.sample(population, k)
        Return a k length list of unique elements chosen from the population sequence or set. 
        Used for random sampling without replacement.  """

"""  random.randint(a, b)
        Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).  """


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


# End of function definitions

# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.

    clear()

    print(f"There are {len(boys_list)} name in the boys list.")

    print(f"There are {len(girls_list)} name in the girls list.")

    all_names = boys_list + girls_list

    all_names_copy = all_names[:]

    all_names_copy.sort()

    print(f"The combined list contains {len(all_names_copy)} boys and girls names.\n")

    # Set the sample size for the list used.
    sample_size = 20

    short_name_list = sample(all_names_copy, sample_size)

    short_name_list.sort()

    print(f"Here is a randomly selected, sorted list of {sample_size} names, \n{short_name_list}\n"
          f" from the list of {len(all_names_copy)} names.")

    """
    Generate a random number appropriate to the number of names in the list.
    Use the random number to retrieve and print the corresponding name from the list.
    Repeat until you have output the correct number of students, as input by the user.
    """

    while True:

        # Setup to request data and convert it to a floating point number,
        #   also prepare for invalid data type.
        try:
            group_count = abs(int(input(f"\nHow many names would you like from the list above? ")))
        except ValueError:
            print(f"Only integers are allowed.")
            continue
        if group_count > sample_size:
            print(f"The largest group size is limited to {sample_size}.")
            continue
        break

    # Create an empty list for the randomly selected small group.
    small_group = []

    for s in range(0, group_count):
        selected_name = short_name_list[randint(0, group_count)]
        short_name_list.remove(selected_name)
        small_group.append(selected_name)

    small_group.sort(reverse=True)
    print(f"\nHere are the {group_count} names selected from the list of {sample_size} and sorted in reverse order: "
          f"\n{small_group}")
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
