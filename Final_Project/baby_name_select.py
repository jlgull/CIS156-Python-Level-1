#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: yet_to_determined.py
#
"""
Final Project Programming Assignment

The project must demonstrate, ALL of the following skills/concepts:

    The project must be your original work. The majority of the Python used must be your own work;
      any code that is based on (or borrowed from) someone else's work must be clearly identified and
      cited both as code comments and in the documentation page below, including specific URLs if applicable.
      You will not receive credit for completing a tutorial or modifying/adapting code from another programmer
      or source.

    The project should consist of a single Python program/script,
      or up to three separate programs that are all related to one another.

    At least one if-statement (with or without elif and else).

    Creation of a function that accepts at least one parameter/argument. This requirement cannot be met using a
      simple "set" method.

    Creation of a function that returns a value--with that returned value used in a meaningful way.
      This requirement cannot be met using a simple "get" method.
      Note: this may be the same function that accepts a parameter for the previous requirement,
        or it may be a different function.

    Use of a loop in a meaningful way. (For example, a loop that iterates only one time before being
      stopped isn't meaningful. Likewise, a loop that iterates multiple times but does nothing
      useful/significant within the project isn't meaningful.)

    Basic exception handling using try-except structures.

    A completed Project Documentation file: CIS156 Final Project Documentation.docx
      In addition to providing basic information, this file is used to ensure that your instructor does
      not miss anything when grading--so it is very important to complete this thoroughly and carefully.

Your project must demonstrate AT LEAST ONE of the following elective skills/concepts:

    A user-defined class (as covered in module 9) used in a meaningful way. The use of inheritance is not required.

    A list or dictionary structure used in a meaningful way

    -or-

    Reading and/or writing files, used in a meaningful way.

"""
#
# Import all required options
#
import json

from random import sample

"""  random.sample(population, k)
        Return a k length list of unique elements chosen from the population sequence or set. 
        Used for random sampling without replacement.  """

from menu_builder import menu

""" This is separate module written to make the menu changes and selection process outside
        of the main body of the program.
"""

from kennedy_13 import clear, get_data

""" This is a module written to contain tools used throughout the main program
        to reduce the duplication of code as the designed moved forward.
        clear() - Performs a screen clear using the OS module and is intended to by Operating System (OS)
                    independent or agnostic.
        get_data    - Is used for all data entry requests. It used try/except to ensure that the data
                        entered is the type expected and it also expects a clarifying question or statement. 
"""


# End of import section


"""

Variable List

Since there are no arrays in Python, so I used a list. Here is information about the (array) List.
List info:
    names           -   This is a dictionary which contains the imported JSON data.
    boys_names      -   The list of boys names, extracted from the names dictionary.
    boys_names_sample   -   The randomly selected list of boys_names used in the final analysis.
    girls_names     -   The list of girls names, extracted from the names dictionary.
    girls_names_sample   -   The randomly selected list of girls_names used in the final analysis.
    combined_names_list     -   The combined list of names, containing both boys and girls names.

String variables:
    In main program:
        do_again    -   Control for repeating the program.
        picked_data -   The string data used in the read statement, which contains the year of the data
                        requested.
        names_json  -   The file handle for the selected year's data.

    In function:
                  
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
        choice      -   The value returned by the menu module, reflecting the data chosen for analysis.
        year        -   The year of the data selected, moved out of the names list.
        sample_size -   The number of names to be randomly extracted from the two list,
                            boys_names and girls names.
        
    In function:
   
"""

#
# Function definition section of the program
#

#
# End of function definitions
#


# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.

    clear(), print()

    while True:
        final_list = []
        print("Please chose the year, to get the popular names for that year.\n")
        choice = menu()


        if choice:
            picked_data = str(choice) + "_baby_name.json"
        else:
            exit()



        # Open the selected JSON data file for analysis.
        with open(picked_data, "r") as names_json:
            # json data in now in a dictionary
            names = json.load(names_json)

            # Read the dictionary data in to lists.
            year = names["year"]
            boys_names = names["boys"]
            girls_names = names["girls"]
            combined_names_list = boys_names + girls_names

            print()
        while True:

            print(f"There are a total {len(boys_names)} names for boys and girls in {year}'s data.\n"
                  f"If you know the gender of your baby, you may select to look only at names for that gender.\n"
                  f"Please enter \"B\" for just boys names, a \"G\" for just girls name or\n"
                  f"a \"C\" for a combined list of both boys and girls names.\n")
            gender_select = get_data("s", "Enter requested gender: ").upper()

            if gender_select != "B" and gender_select != "G" and gender_select != "C":
                print(f"Your must choose be one of the following \"B\", \"G\" or \"C\", pick again. \n")
                continue
            else:
                break

        if gender_select == "B":
            label = "boys"
            chosen_list = boys_names[:]
        elif gender_select == "G":
            label = "girls"
            chosen_list = girls_names[:]
        else:
            label = "combined"
            chosen_list = combined_names_list[:]

        while True:

            print(f"\nFrom the list of {len(chosen_list)}, would you like to find all the names\n"
                  f"starting with a specific set of letters.\n")
            yes_or_no = get_data("s", "If so enter \"Y\" for yes or \"N\" for no. ").upper()

            if yes_or_no != "Y" and yes_or_no != "N":
                print(f"Your must choose \"Y\" or \"N\", pick again. \n")
                continue
            else:
                break

        if yes_or_no == "Y":

            while True:

                print(f"Enter the letters, up to 3, that you would like the names to start with\n")
                select_letters = get_data("s", "Enter the letters now: ").title()

                if len(select_letters) > 3:
                    print(f"Your choice {select_letters} has more that 3 letter, pick again. \n")
                    continue
                else:
                    break

            for x in chosen_list:
                if not x.startswith(select_letters):
                    continue
                final_list.append(x)
            print(f"\nData from the year: {year}.")
            print(f"Here are the {len(final_list)} {label} names starting with \"{select_letters}\", sorted:\n "
                  f"{sorted(final_list)}")

        else:

            while True:

                print(f"\nThere are {len(chosen_list)} {label} names ready for your review in the {year}'s data.\n"
                      f"The sample size will determine how many names are randomly chosen for your review.")
                sample_size = get_data("i", "Enter requested sample size: ")

                if sample_size > len(chosen_list):
                    print(f"Your choice, {sample_size}, is greater than {len(chosen_list)}, pick again. \n")
                    continue
                else:
                    break

            final_list = sample(chosen_list, sample_size)

            print(f"\nData from the year: {year}.")
            print(f"Here are the {sample_size} randomly selected {label} names, sorted:\n {sorted(final_list)}")
        break

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to analyze another year's data? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
