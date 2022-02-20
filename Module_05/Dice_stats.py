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
# Declare the dice dictionary
#

dice_dic = {}       # Will hold the results of the dice rolls

# Enter basic information to run program

num_of_dice = int(input("Enter the number of dice being used: "))

print("Enter the number of rolls of two dice to analyzed.")
num_of_rolls = int(input("\tEnter the negative number to abort stop the program: "))

#
#   Set the dice_dic counters to 0
#

for i in range(num_of_dice, (6 * num_of_dice) + 1):
    dice_dic[i] = 0

#
# Main body of the random dice roll process
#

if num_of_rolls >= 1:
    for roll_counter in range(num_of_rolls):
        # roll the first die
        roll_total = random.randint(1, 6)
        # roll all the rest of the dice
        for num_dice in range(1, num_of_dice):
            roll_total = roll_total + random.randint(1, 6)
            # print("roll total =", roll_total)
        dice_dic[roll_total] += 1
        if num_of_rolls <= 10:
            # print(f'\tRoll {roll_counter} is {roll_total}: ({die1} + {die2})')
            print(f'\tRoll {roll_counter} is {roll_total}')

    # Print the dice roll histogram using a loop
    if num_of_dice == 1:
        print(f'\nHistogram for rolling {num_of_dice} die {num_of_rolls} times\n')
    else:
        print(f'\nHistogram for rolling {num_of_dice} dice {num_of_rolls} times\n')
    for i in range(num_of_dice, (6 * num_of_dice) + 1):

        # print(f'Die {i},\t {dice_dic[i]}')
        print(f'{i}s\t', '*' * dice_dic[i])

else:
    print("\nProgram aborted!!")
