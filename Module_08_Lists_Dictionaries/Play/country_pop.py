#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
population_label = 'Total population'
country_label = "Country"
#
# Define functions
#

def get_key(val):
    for key, value in country_pop.items():
         if val == value:
             return key



user_input = 'China:1365830000,' \
             'India:1247220000,' \
             'United States:318463000,' \
             'Indonesia:252164800'


entries = user_input.split(',')
country_pop = {}
print(entries)

for pair in entries:
    print(pair)
    split_pair = pair.split(':')
    country_pop[split_pair[0]] = int(split_pair[1])
    # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }


print("\nThe solution!\n")

''' Your solution goes here '''

# Setup for sort order query
while True:

    print("What order would you like the list sorted,")
    sort_order = input("\tenter \"L\" for Largest first or \"S\" for Smallest first. ").upper()
    if sort_order == "L" or sort_order == "S":
        break
    else:
        print("Enter either \"L\" or \"S\"")


if sort_order == "L":
    pop_list = sorted(list(country_pop.values()), reverse=True)  # Convert view to list, sorted largest to smallest.
    print("\nPopulation sorted Largest to Smallest.")
else:
    pop_list = sorted(list(country_pop.values()))  # Convert view to list, sorted smallest to largest.
    print("\nPopulation sorted Smallest to Largest.")

# Test print for sorted list concept.
# print(pop_list)

# Title for printed report
print(f'{country_label:^25}{population_label:^16}')

#for country, pop in country_pop.items():
for p_list in pop_list:
    country_key = get_key(p_list)
    # print(f'{country_key} has {country_pop.values():,} people.')
    print(f'{country_key:^25} {country_pop[country_key]:,}')


# End of Program
()