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

num_resistors = 5
resistors = []
voltage_drop = []

print(f'{num_resistors} resistors are in the series.')
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print(input_voltage)

print(f'Input ohms of {num_resistors} resistors')
for i in range(num_resistors):
    res = float(input(f'{i + 1}) '))
    print(res)
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)
print(f'System current is: {current:.4f} amps.')

# Calculate voltage drop over each resistor
# ....
for i in range(num_resistors):
    voltage_drop.append(resistors[i] * current)

# Print the voltage drop per resistor
# ....
for i in range(num_resistors):
    print(f'The voltage drop across resistor {i},  @ {resistors[i]:.2f} Ohm, is {voltage_drop[i]:.3f} Volts.')

# End of Program
