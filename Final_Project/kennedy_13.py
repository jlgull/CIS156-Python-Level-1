#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: kennedy_13.py
#
# This is a module written to contain tools used in other programs
#         to reduce the duplication of code as the designed moved forward.
#         clear() - Performs a screen clear using the OS module and is intended to by Operating System (OS)
#                     independent or agnostic.
#         get_data    - Is used for all data entry requests. It uses try/except to ensure that the data
#                         entered is the correct type, it also expects a clarifying question or statement.

#
# Import all required options
#
# Import system and name from the os module.
from os import system, name
""" name    - The name of the operating system dependent module imported. 
                The following names have currently been registered: 'posix', 'nt', 'java'.
                
    system  - Execute the command (a string) in a subshell. 
                This is implemented by calling the Standard C function system(), and has the same 
                limitations. Changes to sys.stdin, etc. are not reflected in the environment of the
                executed command. If command generates any output, it will be sent to the interpreter
                standard output stream. The C standard does not specify the meaning of the return value 
                of the C function, so the return value of the Python function is system-dependent.            
                
"""

# Import sleep from the time module.
from time import sleep
""" sleep   - Suspend execution of the calling thread for the given number of seconds. 
                The argument may be a floating point number to indicate a more precise sleep time. 
                The actual suspension time may be less than that requested because any caught signal 
                will terminate the sleep() following execution of that signal’s catching routine. 
                Also, the suspension time may be longer than requested by an arbitrary amount because 
                of the scheduling of other activity in the system.

"""

# End of import section

"""

Variable List

List info:
    menu_items      - List to hold menu items.

    In function:
        entered_data    - Value entered in response to data requested.
                            This value may be a "Floating Point" number, an "Integer" number
                            or "String" data.
        picked_choice   - Item picked from the menu list.
        year_choice     - The number being returned to the calling program.

"""


#
# Function definition section of the program
#

def clear():
    # Found on this website: https://www.geeksforgeeks.org/clear-screen-python/
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_data(f_i_s, label):
    # Function to request a numerical data, test for validity and
    # return the entered data.
    # f_i_s     - What type of data is requested, (f) for floating point data,
    #               (i) for integer data or (s) for string data.
    # label     - This is the label displayed when requesting data.
    while True:

        if f_i_s == "f":
            # Setup to request data and convert it to a floating point number,
            #   also prepare for invalid data type.
            try:
                entered_data = float(input(label))
            except ValueError:
                print(f"Only numbers are allowed.")
                continue
            break

        elif f_i_s == "i":
            # Setup to request data and convert it to an integer,
            #   also prepare for invalid data type.
            try:
                entered_data = int(input(label))
            except ValueError:
                print(f"Only Integers are allowed.")
                continue
            break

        else:
            # Setup to request string data,
            #   also prepare for invalid data type.
            try:
                entered_data = input(label)
            except ValueError:
                print(f"General warning, expecting letters.")
                continue
            break

    return entered_data

# End of function definitions


# This is set up to all for testing, during development of the
#   tools in the package.
# Test if this is being used as a script?
if __name__ == "__main__":

    # Set the while control value to "Y".
    do_again = "Y"

    # Use while, regarding the desire to re-run the program.
    while do_again != "N":

        # print out some text
        # print('hello geeks\n'*10)

        print("Requesting floating point data")
        data = get_data("f", "Enter floating point data: ")
        print(data)

        print("Requesting integer data")
        data = get_data("i", "Enter integer data: ")
        print(data)

        print("Requesting string data")
        data = get_data("s", "Enter required string: ")
        print(data)

        # sleep for 2 seconds after printing output
        sleep(2)

        # now call function we defined above
        clear()

        # Ask if the user would like to repeat the program.
        # Also, validate for the correct response.
        while True:
            print("\nWould you like to run the program again? Enter (Y) for yes or (N) for no.", end=" ")
            do_again = input().upper()
            if do_again == "N" or do_again == "Y":
                break
            else:
                print("The only valid entries are either a Y or an N.")

# End of Program
