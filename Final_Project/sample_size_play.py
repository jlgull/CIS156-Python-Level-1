#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
import json

from menu_builder import menu

from kennedy_13 import clear, get_data

#
# Define functions
#

clear(), print()

while True:
    choice = menu()

    if choice == 1:
        picked_data = "2000_baby_name.json"
    elif choice == 2:
        picked_data = "2010_baby_name.json"
    elif choice == 3:
        picked_data = "2020_baby_name.json"
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

        print()
        sample_size = get_data("i", "Enter sample size: ")

        print(f"\nData from the year {year}.")
        print(f"\nFirst {sample_size} boys names are:\n {boys_names[:sample_size]}")
        print(f"\nFirst {sample_size} girls names are:\n {girls_names[:sample_size]}\n")

        combined_names_list = boys_names[:sample_size] + girls_names[:sample_size]

        print(f"There are {len(combined_names_list)} names in the combined list, in a sorted "
              f"order:\n{sorted(combined_names_list[:sample_size * 2])}")

        break
# End of Program
