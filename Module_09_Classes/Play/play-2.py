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

class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

    def calculate_pay(self):
        return self.wage * self.hours_worked

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print(f'Alice:\n Net pay: {alice.calculate_pay():.2f}')

barbara = Employee()
barbara.wage = 11.50
barbara.hours_worked = 20
print(f'Barbara:\n Net pay: {barbara.calculate_pay():.2f}')

print()

# "New" means new compared to previous level
class Shape:
    default_color = 'yellow'
    # New: Change from background_color
    count = 0

    def __init__(self):
        Shape.count += 1
        self.number = self.count
        self.color = self.default_color

    def print_description(self):
        print(self.number, 'of', self.count, '-', self.color)

shape1 = Shape()
shape2 = Shape()
shape2.color = 'magenta'

print(Shape.count)
shape1.print_description()
shape2.print_description()


# End of program
