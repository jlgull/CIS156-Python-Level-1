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


# This function does the same thing as the .replace method; but
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


#
# Main Program
#
entered_phrase = input("\nEnter a phrase or your full name, with spaces: ")
find_char = input("\tEnter the character to find in your phrase or full name (enter for space): ")
if find_char == "":
    find_char = " "
replace_char = input("\tEnter the character to replace in your phrase or full name: ")

# This was created prior to learning about the .replace method. Works fine;
#   but then the function has to be created and tested. chose to leave it in
#   since I had created it.
# final_phrase = replace_character(entered_phrase, find_char, replace_char)

# Use .replace method, instead of the function replace_character
final_phrase = entered_phrase.replace(find_char, replace_char)

caps_lock = None

while caps_lock != "Y":
    print("\nIf you would like the output in all CAPITALS,")
    # Use .upper method, to ensure that only "Y" and "N" are entered.
    caps_lock = input("\tEnter a 'Y' for yes or a 'N' for no! ").upper()
    # caps_lock = caps_lock.upper()
    if caps_lock != "Y" and caps_lock != "N":
        print("The only acceptable responses are \'Y\' or \'N\'.")
    else:
        break

if caps_lock == "Y":
    final_phrase = final_phrase.upper()

print(f"\nThe new phrase is \"{final_phrase}\", from the old phrase \"{entered_phrase}\".")
print(f"\tIn the old phrase, all the characters ( {find_char} ) were replaced with ( {replace_char}\'s).")
if caps_lock == "Y":
    print(f"\tIn addition the entire new phrase was CAPITALIZED, as you requested.")


# End of Program
