#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: read_file.py
#
"""
Generic shell for the CIS156 programs

Ch 12 Programming Assignment, Part A

Create a program called read_file.py that reads the address.txt file linked below into a list.
Then, prompt the user to enter a line number, and display that line from the file.
Keep repeating until the user decides to exit.

File to be used for testing: address.txt Download address.txt .
Note: With most IDEs, you will need to add this file to your project; you can usually drag and drop
    the file to do so.

"""
#
# Import all required options
#
# Import system and name from os
from kennedy_13 import clear, get_data


# End of import section

"""

Variable List

Since there are no arrays in Python, so I used a list. Here is information about the (array) List.
List info:
    address_words       -   This will hold the content of the text file.    

String variables:
    In main program:
        speach          -   File handle assigned during the file open statement.
        address_words   -   A list to contain all of the lines in speach.
        do_again        -   Control for rerunning the program.
        another_line    -   Control for asking for another line.
        
    In function:
                  
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
        line_number     - This is the line to be printed.  
      
    In function:
   
"""

#
# Function definition section of the program
#

# End of function definitions

# Set the while loop control values to "Y".
do_again = another_line = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program. Clear the screen and print a blank line.
    clear(), print()

    # Print a message about what the program does and expected user interaction.
    print(f"This program will open and read from a file named, \'address.txt\'. \n"
          f"Then the program will list how many lines there are and ask you"
          f" for a number to display a specific line.\n")

    # Create a program called read_file.py that reads the address.txt file linked below into a list.
    # Open the file and create the file handle.
    with open("address.txt", "r") as speach:

        # Read the entire file into a list.
        address_words = speach.readlines()

    # Then, prompt the user to enter a line number, and display that line from the file.
    # Setting up to request a specific line number to display.
    print(f"The file \'address.txt\' contains {len(address_words)} lines."
          f"  Which line would you like to see?\n")

    # Use while, regarding the desire to read another line.
    while another_line != "N":

        # Use try to catch if the entered number is greater than the number of lines.
        try:
            line_number = get_data("i", "Enter the line number for the line you would like to read: ")

            # Print the requested line, stripping off any embedded linefeed characters.
            print(f"Line # {line_number}: {address_words[line_number - 1].strip()}")

        # Except to catch if the entered number is greater than the number of lines.
        except IndexError:

            # Message if entered number is greater that the number of lines.
            print(f"Requested number, {line_number}, is greater than the line count of,"
                  f" {len(address_words)} lines.")

            continue

        # Keep repeating until the user decides to exit.
        # Ask if the user would like to read another line.
        # Also, validate for the correct response.
        while True:
            print("\nWould you like to read another line? Enter (Y) for yes or (N) for no.", end=" ")
            another_line = input().upper()
            if another_line == "N" or another_line == "Y":
                break
            else:
                print("The only valid entries are either a Y or an N.")

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to re-run the program? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program.
