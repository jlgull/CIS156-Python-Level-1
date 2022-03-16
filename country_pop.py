#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

#
# Define functions
#

user_input = 'China:1365830000,India:1247220000,United States:318463000,Indonesia:252164800'
entries = user_input.split(',')
country_pop = {}
print(entries)

for pair in entries:
    print(pair)
    split_pair = pair.split(':')
    country_pop[split_pair[0]] = split_pair[1]
    # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }


print("\nThe solution!\n")

''' Your solution goes here '''
for country, pop in country_pop.items():
    # pop_d = "{:,}".format(pop)

    print(f'{country} has {int(pop):,} people.')
# End of Program
