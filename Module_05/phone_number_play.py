#! / bin / python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

user_input = input('Enter phone number: ')
# convert input to all Upper Case
user_input = user_input.upper()
phone_number = ''

for character in user_input:
    if ('0' <= character <= '9') or (character == '-'):
        phone_number += character
    elif ('A' <= character <= 'C'):
        phone_number += '2'
    elif ('D' <= character <= 'F'):
        phone_number += '3'
    elif ('G' <= character <= 'I'):
        phone_number += '4'
    #FIXME: Add remaining elif branches
    else:
        phone_number += '?'

print(f'Numbers only: {phone_number}')

