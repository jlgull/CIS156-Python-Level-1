#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: guess.py
#
"""

Ch 5 Programming Assignment, Part B

Create a simple "guess the number" game in a program called guess.py.
Generate a random number between 1 and 10 and then ask the user to guess it;
let the user know if their guess was high, low, or correct.
Keep repeating until they correctly guess the number.

Note: to generate a random number, see the randint() function in zyBooks 5.3.2.
Don't forget to import random.
If you have trouble getting this to work, you can skip the "randomness"
and just pick a number to be guessed.

"""
#
# Import required module files.
#

import random

# End of import section.
"""
Variable List

String variables:
play_again  - answer to play the game again question, only Y and N are accepted

Floating point numbers:

numbers numbers: 
start_num   - number entered to start summing process
temp_start  - holds start, to be used if start is greater than end
end_num     - number entered to end summing process
temp_end    - holds end, to be used if start is greater than end
random_goal - random number picked by the computer
error_band  - the span of the ending number minus the starting number divided by 3.
                This number is used to add "to" to the "high" or "low" error statement. 
guess       - value entered by user
guess_count - count of tries to match random number
guess_error - how wrong was the guess


"""

#
# Create and Assign default values to the variables.
#
# Setting the default for play_again, as it is used for the while loop containing the whole game.
play_again = "Y"

# Setting the default values for the game.
start_num = 1
end_num = 10

# Setting the
random_goal = 0
guess = 1
guess_count = 0
guess_error = 0


#
# Start the game, this is the return point if the user wishes to play again.
#

while play_again != "N":

    #
    # Reset the starting and ending numbers, needed to return to basic 1 to 10 random play.
    start_num = 1
    end_num = 10

    #
    # Introduce player to the game.
    #
    print(f"\n\nThis game asks you, the player, to guess a number between {start_num} and {end_num}.")
    print('\nThe player does have the option to enter their own unique starting and ending numbers.')
    print('\nThe player\'s starting and ending numbers can be positive or negative numbers.')
    print('\tThe only restriction is the start must be less than the end.')
    print('\tIf the start is greater than the end, the numbers will be switched.')

    # Ask if the player would like to enter their own starting and ending numbers.
    #   If they want to, request their numbers.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to enter your own starting and ending numbers?")
        play_again = input("\tIf so, enter (Y) for yes or (N) for no. ")
        play_again = play_again.upper()
        if play_again == "N" or play_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

    #
    # If the user wants to enter their own numbers,
    #   ask the user for the starting and ending numbers, also capture the numbers
    #   in case the starting number is greater than the ending number.
    if play_again == "Y":
        temp_start = start_num = int(input("\nPlease enter the starting number: "))
        temp_end = end_num = int(input("\tNow enter the ending number:  "))

        # If the starting number is greater than the ending number, switch the numbers.
        if temp_start > temp_end:
            end_num = temp_start
            start_num = temp_end

    # Set goal to something larger that ending number to ensure that play starts.
    guess = end_num * 355 / 113   # Note, 355/113 is a fair approximation of pi!!

    # Generate the random number (number) using the random module object, randint.
    #   The random number used the starting and ending numbers, to determine the range of
    #       the random number generated.
    random_goal = random.randint(start_num, end_num)

    #   Calculate error band value, from the starting and ending numbers and using floor division.
    error_band = (end_num - start_num) // 3

    # This print line was for testing. It will be removed or commented out when finished.
    # print(f'Start: {start_num} End: {end_num} Random number: {random_goal} and Error {error_band}')

    #
    # Start the guessing portion of the program.
    #
    # Resetting the guess count, important if playing the program more than once.
    guess_count = 0

    while guess != random_goal:
        guess = int(input("Enter your guess: "))
        guess_count += 1

        # Test guess and if wrong, give directional feedback.
        if guess != random_goal:
            guess_error = abs(guess - random_goal)
            if guess_error > error_band:
                if guess > random_goal:
                    print(f'Your entry of {guess}, was Too High.')
                else:
                    print(f'Your entry of {guess}, was Too Low.')
            else:
                if guess > random_goal:
                    print(f'Your entry of {guess}, was High.')
                else:
                    print(f'Your entry of {guess}, was Low.')

        # When the guess is correct, report the results.
        if guess == random_goal:
            if guess_count == 1:
                print(f"\nGreat job, you guessed the random number: {random_goal} in {guess_count} try.")
            else:
                print(f"\nGreat job, you guessed the random number: {random_goal} in {guess_count} tries.")

    # The following code as copied from the sum_loop program.
    # Ask if the user would like to play the game again?
    # Also, validate for the correct response.
    while True:
        play_again = input("\nWould you like to play the game again? Enter (Y) for yes or (N) for no. ")
        play_again = play_again.upper()
        if play_again == "N" or play_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
