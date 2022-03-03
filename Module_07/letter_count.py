#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: letter_count.py
#
"""
Generic shell for the CIS156 programs

Ch 7 Programming Assignment, Part A

Create a program in a file named letter_count.py.
Prompt the user to enter three different words or phrases, one at a time;
    store each response in a separate variable.
Next, prompt the user a letter they wish to count.
Finally, count how many times the letter occurs in each of the three words/phrases,
    regardless of case (uppercase or lowercase), as well as the total;
    output a formatted table displaying the results.
Be sure your program includes adequate directions for the user.

"""

"""

Variable List

List info:
    word_list       -   Contains the words entered, that will have letters counted in them
    letter_count    -   Contains the count of the requested letter in each of the words.

String variables:
    In main program:
        do_again        -   Used to control the repeating of the program.
        count_letter    -   The letter to be counted in each word.
        total_title     -   The title for the print section.
        num_of_entries  -   The string entry from input, regarding the number of words to enter.
    
    In function:
                  
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
        num_entries  -   Contains the integer count of the words to be entered and reviewed
      
    In function:
   
"""

# Define initial value of required variables.

total_title = "Total occurrences"


# Function definition section of the program if any functions are required.
#   No functions in this program.

# General print statement about what te program does.
print("\nThis program will ask you how many words or phrases you would like to enter,")
print("\tif you simply hit enter, the default will be 3 words or phrases.")
print("Then the program will ask you for the words or phrases you would like to enter.")
print("Finally the program will ask you for the letter to count in words or phrases you enter.")


# Use while, regarding the desire to re-run the program.
# Set the while control value to "Y".
do_again = "Y"
while do_again != "N":

    # Set or Reset variables prior to each run.
    word_list = list()
    letter_count = list()
    letter_count_total = 0
    num_of_entries = 0

    # Main body of the program.

    num = "Y"
    while num != "N":

        # Prompt the user to enter three different  words or phrases, one at a time;
        #   store each response in a separate variable.
        # Find out how many words or phrases the user want to enter.
        print("\nEnter how many words would you like to enter?")
        print("\tIf you hit enter, without entering a number, the system will default to 3: ", end="")
        num_of_entries = input()
        if num_of_entries.isnumeric():
            num_entries = int(num_of_entries)
            break
        elif len(num_of_entries) == 0:
            num_entries = 3
            break
        else:
            print("You must enter a number or simply press \"Enter\".")

    # Enter as many words or phrases as you asked for.
    for i in range(1, num_entries + 1):
        print(f"Please enter word or phrase {i}: ", end="")
        word_list.append(input())

    # Next, prompt the user for a letter they wish to count.
    # Now you get to enter the symbol or letter to be counted.
    print("\nWhen entering the symbol or letter you wish to count, you may disregard the case")
    print("\tin both the words or phrase entered and the symbol or letter you would like to count." )
    count_letter = input("\nEnter the symbol or letter you would like to count? ")

    """
    Finally, count how many times the letter occurs in each of the three words/phrases,
        regardless of case (uppercase or lowercase), as well as the total;
        output a formatted table displaying the results.
    """
    # Count the occurrences of the letter you entered, in the words or phrases you entered.
    for i in range(num_entries):
        letter_count.append(word_list[i].upper().count(count_letter.upper()))

        # This creates the letter_count_total.
        letter_count_total = letter_count_total + letter_count[i]

    # Put a header on for the results print out, of the count process.
    print(f"\nHere are the results of this program.")
    print(f"\nFor the {num_of_entries} words or phrased you entered,")
    print(f"\there is the count of the character ({count_letter}),")
    print(f"\tas well as a total count in all {num_entries} words or phrased you entered.")

    # Draw a line above the counted results.
    print("-" * 40)

    # Print out the results of the count process.
    for i in range(num_entries):
        print(f"\t{word_list[i]:<25}{letter_count[i]:>10}")

    # Draw a line above the counted results.
    print("-" * 40)
    print(f"\t{total_title:<25}{letter_count_total:>10}")

    # Ask if the user would like to play again.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to play again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
