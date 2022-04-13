#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: envelope.py
#
"""
Generic shell for the CIS156 programs

Ch 12 Programming Assignment, Part B

Create a program called envelope.py that prompts the user to input the following,
    storing each in a separate variable:

    Recipient's name
    Address
    City
    State
    Zip Code

Then, the program should create a new file called envelope.txt with a rudimentary mailing envelope:
    Your name and return address at the top-left followed by the recipient's name and address.

Sample output file:

Jose Pena
123 Main St.
Avondale, AZ 85392


          Yuri Davidson
          456 Pine Ave
          Litchfield Park, AZ 85393


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
    return_address      -   The return address for the letter to be sent, set to the author's address.
    gathered_address    -   The address entered for the outgoing letter.
    outgoing_address    -   The address to be printed on the outgoing letter.

String variables:
    In main program:

    In function:
                  
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
      
    In function:
   
"""

#
# Function definition section of the program
#


# End of function definitions

# Set the while control value to "Y".
do_again = "Y"

# Establish the return_address list.
return_address = list()

# Establish the return address.
return_address.append("Jonathan Heard")
return_address.append("10717 W. Flower Ave.")
return_address.append("Avondale, AZ")
return_address.append("85392")

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program, clear the screen and print a blank line.
    clear(), print()

    # Establish the gathered_address and the outgoing_address list, will also clear for a repeat execution.
    gathered_address = []
    outgoing_address = []

    # Explain the purpose of the program.
    print(f"This program will collect an address you would like to use, to mail a letter.\n"
          f"Then the address you entered will be written to a file for future printing.\n"
          f"My address, as the author of the program, will be set at the return address.\n")

    # Prompts the user to input the following, storing each in a separate variable:
    #     Recipient's name
    #     Address
    #     City
    #     State
    #     Zip Code
    # Gather the outgoing address information.
    gathered_address.append(get_data("s", "Enter the Recipient's name: "))
    gathered_address.append(get_data("s", "Enter the Recipient's Address: "))
    gathered_address.append(get_data("s", "Enter the Recipient's City "))
    gathered_address.append(get_data("s", "Enter the Recipient's State: "))
    gathered_address.append(get_data("s", "Enter the Recipient's zip code: "))

    # Format the outgoing address.
    outgoing_address.append(gathered_address[0].title())
    outgoing_address.append(gathered_address[1].title())
    outgoing_address.append(gathered_address[2].title() + ", " + gathered_address[3].upper())
    outgoing_address.append(gathered_address[4].upper())


    # Then, the program should create a new file called envelope.txt with a rudimentary mailing envelope:
    # Your name and return address at the top-left followed by the recipient's name and address.
    # Set up to write the 2 addresses to a file.

    # Print a blank line above the return address.
    print()

    # Print the return address in the Upper left corner of the
    for t in range(len(return_address)):
        print(return_address[t])

    # Print a blank line between the 2 addresses.
    print()

    # Print the outgoing address 10 spaces in from the left margin.
    for x in range(len(outgoing_address)):
        print(" " * 10, outgoing_address[x])

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to enter different address? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
