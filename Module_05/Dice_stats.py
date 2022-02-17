#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

import random

#
# Declare and set variables
#

dice_dic = {} # Will hold the results of the dice rolls
num_of_dice = 2 #int(input("Enter the number of dice being used:\n"))
print("Enter the number of rolls of two dice to analyzed.")
num_of_rolls = int(input("\tEnter the negative number to abort stop the program: "))
# row_star = "*"*x
# print("*" * x)
#

#
#   Set the dice_dic counters to 0
#

for i in range(num_of_dice, (6 * num_of_dice) + 1):
        dice_dic[i] = ""

#
# Main body of the random dice roll process
#

if num_of_rolls >= 1:
    for roll_counter in range(num_of_rolls):
        die1 = random.randint(1 , 6)
        die2 = random.randint(1, 6)
        roll_total = die1 + die2
        dice_dic[roll_total] += "*"
        if num_of_rolls <= 10:
            print(f'\tRoll {roll_counter} is {roll_total} ({die1} + {die2})')

    # print("\nRaw dice analysis data:", dice_dic)

    # Print the dice roll histogram

    print(f'\nDice roll histogram, for {num_of_rolls} rolls\n')
    for i in range(num_of_dice, (6 * num_of_dice) + 1):
            print(f'Die {i},\t {dice_dic[i]}')

else:
    print("Program aborted!!")
