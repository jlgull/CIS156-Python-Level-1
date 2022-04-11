#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# This file, kennedy_13.py will be a basic toolbox for projects to come.
#    As new tools are developed, they will be added here.
#    The first tool here is the clear screen module.
#    Others will be added and fine-tuned as the course moves along.
#

#
# Import all required options
#
# Import system and name from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# End of import section

#
# Function definition section of the program
#


def clear():
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# End of function definitions


# Test if this is being used as a script?
if __name__ == "__main__":

    # print out some text
    print('hello geeks\n'*10)

    # sleep for 2 seconds after printing output
    sleep(2)

    # now call function we defined above
    clear()

# End of Program
