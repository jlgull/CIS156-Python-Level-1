#! / bin / python3
#
# Author: Jonathan Heard
# Work for CIS156, Spring 2022, based on zyBook, CIS156: Python Programming: Level 1
#
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# 1) Program taken from zyBook, Chapter 1, Paragraph 1-4-2

triangle_base = 0  # Triangle base (cm)
triangle_height = 0  # Triangle height (cm)

# Triangle area (cm**2)

print('Enter triangle base (cm): ')

triangle_base = int(input())

# 2)

print('Enter triangle height (cm): ')

triangle_height = int(input())

# Calculate Triangle Area

triangle_area = (triangle_base * triangle_height) / 2

# Print out Triangle base, height and area

# 3)

print('Triangle area = (', end=' ')

print(triangle_base, end=' ')

print('*', end=' ')


print(triangle_height, end=' ')

print(') / 2 = ', end=' ')

print(triangle_area, end=' ')

print('cm**2')