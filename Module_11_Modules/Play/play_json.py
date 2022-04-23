#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

from kennedy_13 import clear

# importing the module
from json import load


#
# Define functions
#



# Python program to demonstrate
# Conversion of JSON data to
# dictionary



# Opening JSON file
with open('2020_baby_names.json') as json_file:
    data = load(json_file)

    clear()
    # for reading nested data [0] represents
    # the index value of the list
    print(f"\n{type(data)}\n")

    for i in range(0, 1000, 100):

        print(i, data['girls'][i])
        print(i, data['boys'][i])

    # for printing the key-value pair of
    # nested dictionary for loop can be used
    #print("\nPrinting nested dictionary as a key-value pair\n")
    #for i in data['people1']:
    #    print("Name:", i['name'])
    #    print("Website:", i['website'])
    #    print("From:", i['from'])
    #    print()




# End of program
