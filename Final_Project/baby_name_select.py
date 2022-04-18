#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: baby_name_select.py
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

""" JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, 
        is a lightweight data interchange format inspired by JavaScript object literal syntax 
        (although it is not a strict subset of JavaScript 1 ).
        json exposes an API familiar to users of the standard library marshal and pickle modules.
"""

from random import sample

"""  random.sample(population, k)
        Return a k length list of unique elements chosen from the population sequence or set. 
        Used for random sampling without replacement.
"""

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

List info:
    names           -   This is a dictionary which contains the imported JSON data.
    boy_names      -   The list of boy names, extracted from the names dictionary.
    girl_names     -   The list of girl names, extracted from the names dictionary.
    combined_names_list     -   The combined list of names, containing both boy and girl names.
    chosen_list     -   The list created, based on the gender selection. May contain just the boy names,
                            the girl names or both lists added together.
    final_list      -   The last list built, based on the answer to all the questions.

String variables:
    In main program:
        do_again    -   Control value for repeating the program.
        names_json  -   The file handle for the selected year's data.
        picked_data -   The string data built to be used in the read statement, which contains the year of the 
                        data requested.
        label       -   Defines if the data if for boy, girl or combined data.
        gender_select   -   Value returned, regarding the choice of gender for which data set to review.
        yes_or_no   -   Controls entering the starting letters of the name or going to the random selection
                            process.
        selected_letters    -   The requested starting letters for the search for names starting with specific
                                    letters, limit is 3 letters.
        x                   -   The looping variable, to find names that start with the selected_letters.                            
                 
Floating point numbers: None in this program or script.
    
Integers numbers: 
    In main program:
        choice      -   The value returned by the menu module, reflecting the data chosen for analysis.
        year        -   The year of the data selected, moved out of the names list.
        sample_size -   The number of names to be randomly extracted from the list of names.
        
    
"""

#
# Function definition section of the program.
#
#   No new functions in this program or script.
#
# End of function definitions.
#


# Set the while control value to "Y".
do_again = "Y"

# Clear the screen at the start of the program.
clear()

print(f"\nThis program presents a list of the 1000 most popular boy or girl names from\n"
      f"    2000, 2010 or 2020. The user first gets to choose the year they would like to look through.\n"
      f"  Next, if they know the gender of there child, they can restrict the rest of the work to\n"
      f"    just that gender or a combined list of both genders.\n "
      f"  Finally they can either look for names starting with specific letters, up to 3, or\n"
      f"    get a random sample of their chosen list.\n"
      f"  In theory, the user could get all 2000 names in the combined list; but that is not a very useful option.")


# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.

    # clear()

    # Start the information gathering, first determine the year to be reviewed.
    while True:
        final_list = []
        print("\nPlease chose a year, to get the popular names for that year.\n")
        choice = menu()

        if choice:
            picked_data = str(choice) + "_baby_name.json"
        else:
            exit()

        # Bring in the data for the year chosen by first,
        #   opening the selected JSON data file for analysis.
        with open(picked_data, "r") as names_json:
            # json data in now in a dictionary
            names = json.load(names_json)

            # Read the dictionary data in to lists.
            year = names["year"]
            boy_names = names["boys"]
            girl_names = names["girls"]
            combined_names_list = boy_names + girl_names

        # Find out from the user whether they want a specific gender or a combined list.
        while True:
            print(f"\nThere are a total of {len(boy_names)} boy names and {len(girl_names)} girl in the "
                  f"{year} data.\n"
                  f"If you know the gender of your baby, you may select to look only at names for that gender.\n"
                  f"Please enter \"B\" for just boy names, \"G\" for just girl names or\n"
                  f"\"C\" for a combined list of both boy and girl names.\n")
            gender_select = get_data("s", "Enter requested gender: ").upper()

            if gender_select != "B" and gender_select != "G" and gender_select != "C":
                print(f"Your must choose be one of the following \"B\", \"G\" or \"C\", pick again. \n")
                continue
            else:
                break

        if gender_select == "B":
            label = "boy"
            chosen_list = boy_names[:]
        elif gender_select == "G":
            label = "girl"
            chosen_list = girl_names[:]
        else:
            label = "combined"
            chosen_list = combined_names_list[:]

        # Find out if the user would like to search for a names starting with specific letters, up to 3.
        while True:
            print(f"\nFrom the list of {len(chosen_list)} {label} names, would you like to find all the names\n"
                  f"starting with a specific set of letters.\n")
            yes_or_no = get_data("s", "If so enter \"Y\" for yes or \"N\" for no. ").upper()

            if yes_or_no != "Y" and yes_or_no != "N":
                print(f"Your must choose \"Y\" or \"N\", pick again. \n")
                continue
            else:
                break

        if yes_or_no == "Y":

            # If there is a desire to search for names starting with up to 3 letters, gather the letters.
            while True:
                print(f"\nEnter the letters, up to 3, that you would like the names to start with\n")
                select_letters = get_data("s", "Enter the letters now: ").title()

                if len(select_letters) > 3:
                    print(f"Your choice {select_letters} has more that 3 letter, pick again. \n")
                    continue
                else:
                    break

            # Loop through the chosen_list with the letters entered, using the .startswith string method
            #   to create the final_list.
            for x in chosen_list:
                if not x.startswith(select_letters):
                    continue
                final_list.append(x)

        else:

            # If there is no desire to search with specific letters, find what sample size to use for
            #   the random sample size process.
            while True:

                print(f"\nThere are {len(chosen_list)} {label} names ready for your review in the {year}'s data.\n"
                      f"The sample size will determine how many names are randomly chosen for your review.")
                sample_size = get_data("i", "Enter requested sample size: ")

                if sample_size > len(chosen_list):
                    print(f"Your choice, {sample_size}, is greater than {len(chosen_list)}, pick again. \n")
                    continue
                else:
                    break

            # Us the random.sample tool to build the final_list.
            final_list = sample(chosen_list, sample_size)

        # Print out the final report on the data requested. Using the yes_or_no variable to select
        #   which print statement to use for the final data.
        print(f"\nData from the year: {year}.")
        if yes_or_no == "Y":
            print(f"Here are the {len(final_list)} {label} names starting with \"{select_letters}\", sorted:\n "
                  f"{sorted(final_list)}")
        else:
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
