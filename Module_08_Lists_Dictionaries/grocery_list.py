#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: grocery_list.py
#
"""

Ch 8 Programming Assignment, Part A

Create a program called grocery_list.py that allows the user to input a list of items to buy at the
    supermarket. It should begin by asking the user to input the number of items to add to the list.
    Then, it should use a loop to prompt the user to input that many items, storing each in the list.
    After the items have been entered, it should output the full list.

"""

#
# Import all required options
#
# Import system and name from os
from os import system, name

# End of Import Section


"""

Variable List

Since there are no arrays in Python, so I used a list. Here is information about the (array) List.
List info:
    In main program:
    grocery_list    -   List variable to hold grocery list to be bought.
    sorted_grocery_list - Sorted grocery list.


String variables:
    In main program:
        do_again    - Holds flag for the while loop, regarding the re-execution of the program.
        print_label - The label for the printing job.

    In function:
        name    - Information returned by the system, to identify type of OS
                      
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
        list_count  - Number of items in the list
      
    In function:
   
    
"""

# Function definition section of the program


def clear():
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is "posix")
    else:
        _ = system("clear")
#
# End of function definition section


# Fixed variable definitions
print_label = "Here is your grocery list, sorted:"

# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Preset variables used during the program
    grocery_list = list()
    list_count = 0

    # Clear screen to begin program.
    clear()

    # Needed to determine the length of the print label,
    # will be commented out, once determined.
    # print(len(print_label))

    # Main body of the program.

    # It should begin by asking the user to input the number of items to add to the list.
    # Chose to not ask; but rather stop when there is no entry.

    print("\nThis program will ask for item for your grocery list.")
    print("\nThere will be no need to know how many items are on your list,")
    print("\tsince the program will continue to ask for items, until you simply hit")
    print("\t\"Enter\" with no item entered.\n")

    #  Then, it should use a loop to prompt the user to input that many items, storing each in the list.
    while True:
        entered_item = input("Enter item for you shopping list, simply hit \"Enter\" to stop. : ")
        if len(entered_item) == 0:
            break
        else:
            grocery_list.append(entered_item)
            list_count += 1

    # After the items have been entered, it should output the full list.

    # Sort the list, prior to presentation
    sorted_grocery_list = sorted(grocery_list)

    # Print out the grocery list.
    print(f"\n{print_label}")
    for i in range(list_count):
        print(f"{sorted_grocery_list[i]:^34}")

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to create a new grocery list? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print(f"\nYour entry of, \"{do_again}\" is not a valid entry.")
            print("The only valid entries are either a Y or an N.")

# End of program
