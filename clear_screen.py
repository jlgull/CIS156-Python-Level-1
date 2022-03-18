#!/etc/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# End of import section

#
# Function definition section of the program
#


def clear():
    # define our clear function

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# End of function definitions


# print out some text
print('hello geeks\n'*10)

# sleep for 2 seconds after printing output
sleep(2)

# now call function we defined above
clear()

# End of Program
