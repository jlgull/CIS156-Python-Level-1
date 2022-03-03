#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: name_modifier.py
#
"""
Generic shell for the CIS156 programs

Ch 7 Programming Assignment, Part B

Create a program that accept a person's full name,
    and then convert that sentence to all caps with underscore characters in place of any spaces
    and output the result.
Be sure to give the user adequate instructions for using the program.
Name the file name_modifier.py.

"""

"""

Variable List

List info:


String variables:
    In main program:
        entered_phrase  -   The name or phrase to be manipulated.
        find_char       -   The character to be found and replaced in the entered word or phrase.
        replace_char    -   The replacement character, to be put into the entered word or phrase.
        caps_lock       -   The flag to set the entire output to CAPITAL letters.
        
    In function:
                  
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
      
    In function:
   
"""
# Function definition section of the program if any functions are required.
# This function does the same thing as the (.replace) method; but
#   since I had it working, prior to learning about the .replace method,
#   I am leaving it in. Could be useful at some further time.


def replace_character(word, find, replace):
    new_word = ''
    for character in word:
        if character != find:
            new_word = new_word + character
        else:
            new_word = new_word + replace
    return new_word


# General print statement about what te program does.
print("\nThis program will ask you to enter either your full name or a phrase.")
print("\tThen the program will ask you for a character, in the words or phrases, that you would like to replace.")
print("\tNext the program will ask you for a replacement character.")
print("\tThe last question is whether you would like the entire output in CAPITAL letters.")

#
# Main Program
#

# Use while, regarding the desire to re-run the program.
#   Set the while control value to "Y".
do_again = "Y"
while do_again != "N":

    # Create a program that accept a person's full name.
    #   Here is where you enter the name or phrase to be manipulated.
    entered_phrase = input("\nEnter your full name or a phrase, with spaces: ")

    # Now gather the information about what manipulations are to be
    #   done to the entered name or phrase.
    print("\nThe character replacement process is case sensitive, if a letter is entered.")
    find_char = input("\tEnter the character to find in your full name or phrase, (\"Enter\" for a space): ")
    if find_char == "":
        find_char = " "
    replace_char = input("\tEnter the character to replace in your full name or phrase, (\"Enter\" for a \"_\"): ")
    if replace_char == "":
        replace_char = "_"

    # This was created prior to learning about the (.replace) method. Works fine;
    #   but then the function has to be created and tested. Chose to leave it in
    #   since I had created it.
    # final_phrase = replace_character(entered_phrase, find_char, replace_char)

    # Use .replace method, instead of the function replace_character
    final_phrase = entered_phrase.replace(find_char, replace_char)

    # Then convert that sentence to all caps, if requested to.
    caps_lock = None

    while caps_lock != "Y":
        print("\nIf you would like the output in all CAPITALS,")

        # Use .upper method, to ensure that only "Y" and "N" are entered.
        caps_lock = input("\tEnter a 'Y' for yes or a 'N' for no! ").upper()
        if caps_lock != "Y" and caps_lock != "N":
            print("The only acceptable responses are \'Y\' or \'N\'.")
        else:
            break
    # If requested, us (.upper) method to CAPITALIZE the output.
    if caps_lock == "Y":
        final_phrase = final_phrase.upper()

    #   Finally, output the results.
    print(f"\nThe new phrase is \"{final_phrase}\", from the old phrase \"{entered_phrase}\".")
    print(f"\tIn the old phrase, all the characters ( {find_char}'s ) were replaced with ( {replace_char}\'s).")
    if caps_lock == "Y":
        print(f"\tIn addition the entire new phrase was CAPITALIZED, as you requested.")

    # Ask if the user would like to play again.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to play again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

#
# End of program
#
