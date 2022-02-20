#!/bin/python3

# Tracy Baker
# CIS156 online - Tim McMichael
# module 5, part B programming assignment
# Feb. 17, 2022

# Create a simple "guess the number" game in a program
# called guess.py. Generate a random number between
# 1 and 10 and then ask the user to guess it; let the

# user know if their guess was high, low, or correct.
# Keep repeating until they correctly guess the number.

# Import module(s); initialize variable(s)
import random
guess = 0
num_guesses = 0
minimum = 1
maximum = 10
total_guesses = {'H':0, 'C1':0, 'C2':0, 'C3':0}

print("\n\nWelcome to Tracy Baker's extraordinary Pick a Number, Enhanced (PaNE) game!")
print('\nYou (the human) will try to pick a number between 1 and some other number.')
print('(10, by default) in fewer guesses than the computer, which will use three')
print('different methods.')

answer = input('\n\nDo you want to pick the high-side (maximum) number [y = yes, otherwise 10 will be used]: ')
if answer == 'y':
    maximum = int(input('\nEnter a new high-side number: '))

number = random.randrange(minimum, maximum)
print('\nThe number you are to guess has been chosen!')

while True:
    num_guesses += 1
    guess = int(input(f'\nGuess a number from {minimum} to {maximum}: '))

    if guess < minimum or guess > maximum:
        print(f'\nI said from 1 to {maximum}, not {guess}, try again!\n')
    else:
        print('\n\nYour guess is...', end=' ')

        if guess < number:
            print('Too low!')
        elif guess > number:
            print('Too high!')
        else:
            print('Just right!')
            break

print(f'\nCongrats! You guessed {number} in {num_guesses} tries!\n\n')
total_guesses['H'] = num_guesses

print("\n\nNow you'll have the opportunity to see the computer guess the number in three different ways.")

answer = input('\nHave the computer use just random numbers find the number [y = yes]? ')

if answer == 'y':
    num_guesses = 0

    while True:
        num_guesses += 1
        computer_guess = random.randrange(minimum,maximum)

        print(f'\nThe pick is {computer_guess}, which is...', end=' ')

        if computer_guess != number:
            print('Wrong!')
        else:
            print('Just right!')
            break

    print(f'\nThe computer picked {number} in {num_guesses} tries!')
    total_guesses['C1'] = num_guesses

answer = input('\n\nHave the computer use random numbers and bracketing to find the number [y = yes]? ')

if answer == 'y':
    comp_bracket_max = maximum
    comp_bracket_min = minimum
    num_guesses = 0

    while True:
        num_guesses += 1
        computer_guess = random.randrange(comp_bracket_min,comp_bracket_max)

        print(f'\nThe pick is {computer_guess}, which is...', end=' ')

        if computer_guess < number:
            print('Too low!')
            comp_bracket_min = computer_guess + 1
        elif computer_guess > number:
            print('Too high!')
            comp_bracket_max = computer_guess
        else:
            print('Just right!')
            break

    print(f'\nThe computer picked {number} in {num_guesses} tries!')
    total_guesses['C2'] = num_guesses

answer = input('\n\nHave the computer find the number in a deterministic manner (no random numbers) [y for yes]? ')

if answer == 'y':
    num_guesses = 0
    minimum = 0

    while True:
        num_guesses += 1

        computer_guess = (maximum + minimum) // 2

        print(f'\nPicking between {minimum} and {maximum}:')
        print(f"({minimum} + {maximum}) // 2 equals {computer_guess}, which is...", end=' ')

        if computer_guess < number:
            print('Too low!')
            minimum = computer_guess
        elif computer_guess > number:
            print('Too high!')
            maximum = computer_guess
        else:
            print('Just right!')
            break

    print(f'\nThe computer picked {number} in {num_guesses} tries!')
    total_guesses['C3'] = num_guesses

print(f"\n\nYou (the human), found the number in {total_guesses['H']} tries.")
print(f"The computer, using only random numbers, found the number in {total_guesses['C1']} tries.")
print(f"The computer, using random numbers and bracketing, found the number in {total_guesses['C2']} tries.")
print(f"The computer, using no random numbers, found the number in {total_guesses['C3']} tries.")

print('\n\nThank you for playing PaNE, Goodbye!\n\n')