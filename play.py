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


url = input('Enter Wikipedia URL: ')

tokens = url.split('/')

print(tokens)


if 'wiki' != tokens[3]:
    tokens.insert(3, 'wiki')
    new_url = '/'.join(tokens)

    print(f'{url} is not a valid address.')
    print(f'Redirecting to {new_url}')
else:
    print(f'Loading {url}')

# End of Program
