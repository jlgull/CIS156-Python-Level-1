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

student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'): "
delete_prompt = "Enter name of Student to be deleted: "
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n\n")

while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        print()
        name, grade = input(grade_prompt).split()
        # Your code here
        student_grades[name] = grade
    elif command == '2':
        # Your code here
        print()
        name = input(delete_prompt)
        del student_grades[name]
    elif command == '3':
        # Your code here
        print()
        for i in student_grades:
            print(f'The Grade for {i} is {student_grades[i]}')
        print()
    elif command == '4':
        clear()
        print("Thanks for using this Grade Book App!")
        break
    else:
        print('Unrecognized command.')


# End of Program
