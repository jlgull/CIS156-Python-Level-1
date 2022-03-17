#!/etc/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

#
# Define functions
#


def clear():
    # define our clear function

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#
# End of function definition
#

#
# Start of program body
#
# Clear screen
clear()
print()

grades = {
    'John Ponting': {
        'Homeworks': [79, 80, 74],
        'Midterm': 85,
        'Final': 92
    },
    'Jacques Kallis': {
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': {
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

user_input = input('Enter student name: ')

while user_input != 'exit':
    if user_input in grades:
        # Get values from nested dict
        homeworks = grades[user_input]['Homeworks']
        midterm = grades[user_input]['Midterm']
        final = grades[user_input]['Final']

        # print info
        for hw, score in enumerate(homeworks):
            print(f'Homework {hw}: {score}')

        print(f'Midterm: {midterm}')

        print(f'Final: {final}')

        # Compute student total score
        total_points = sum([i for i in homeworks]) + midterm + final

        print(f'Final percentage: {100 * (total_points / 500.0):.1f}%')

    user_input = input('Enter student name: ')

# End of Program
