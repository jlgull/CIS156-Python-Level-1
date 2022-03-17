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
user_input = 'Spain:Madrid,Togo:Lome,Prussia: Konigsberg'
entries = user_input.split(',')
country_capital = {}

for pair in entries:
    split_pair = pair.split(':')
    country_capital[split_pair[0]] = split_pair[1]
    # country_capital is a dictionary, Ex. { 'Germany': 'Berlin', 'France': 'Paris'

''' Your solution goes here '''
del country_capital['Prussia']

print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Spain deleted?', end=' ')
if 'Spain' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Togo deleted?', end=' ')
if 'Togo' in country_capital:
    print('No.')
else:
    print('Yes.')
# End of Program
