#!/etc/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#
"""
Write a program that uses the keys(), values(), and/or items() dict methods to find statistics
    about the student_grades dictionary. Find the following:

    Print the name and grade percentage of the student with the highest total of points.
    Find the average score of each assignment.
    Find and apply a curve to each student's total score,
        such that the best student has 100% of the total points.

"""
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

student_grades_avg = dict()
student_grades_sum = dict()

# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

# Print the name and grade percentage of the student with the highest total of points.

for name in student_grades.keys():
    student_grades_sum[name] = sum(list(student_grades[name]))
    student_grades_avg[name] = sum(list(student_grades[name])) / len(list(student_grades[name]) * 100)
    print(f'Student {name} received an average grade of, \t{student_grades_avg[name] * 100:.2f} %')

# End of Program
