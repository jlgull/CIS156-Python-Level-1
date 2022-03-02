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


def count(word,letter):
    count = 0
    for character in word:
        if character == letter:
            count += 1
    print(f"The letter '{letter}' appears {count} times in the word ({word}).")



count('banana', 'a')

# End of Program
