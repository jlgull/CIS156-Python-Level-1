#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
import json


#
# Define functions
#

sample_size = int(input("Enter sample size: "))


with open("baby_names.json", "r") as names_json:

    # json data in now in a dictionary
    names = json.load(names_json)

    y = names["year"]
    b = names["boys"]
    g = names["girls"]

    print(f"Data from the year {y}:\nfirst {sample_size} boys names, {b[:sample_size]}\nfirst {sample_size} girls names, {g[:sample_size]}\n")

    t = b[:sample_size] + g[:sample_size]


    print(len(t))

    # t.sort()


    print(f"Names from the combined list, sorted:\n{sorted(t[:sample_size*2])}")

    """
    print(names,"\n")

    print(f"Type of 'names' is {type(names)}.\n")

    print(f"Length of 'names' is {len(names)}.\n")

    simple_key = list(names.keys())

    print(f"Type of 'simple_key' is {type(simple_key)}.\n")

    print(f"Simple list of 'names' keys is {simple_key}. \n")

    simple_values = list(names.values())

    print(f"Type of 'simple_values' is {type(simple_values)}.\n")

    print(f"Simple list of 'simple_values' values is {simple_values}. \n")

    girls_names = []
    boys_names = []


    for year, gender in names.items():
        print(f"For the year: {year}\n")
        if year == 'girls':
            girls_names.insert(0, gender[:])
        if year == 'boys':
            boys_names.insert(0, gender[:])


# print(type(full_names))

print(girls_names, boys_names)

all_names = girls_names + boys_names

print(all_names)

    all_names = []

    for value in names.values():
        if isinstance(value, list):
            all_names += value

# all_names.sort(reverse=True)

print(f"\nJason's list, sorted in reverse:\n{sorted(all_names, reverse=True)}")

"""

    #print(girls_names)
# End of Program
