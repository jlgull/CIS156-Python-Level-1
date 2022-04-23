#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

"""
Program to test concept of singular function to do temperature
    conversion, based on the temperature entered.

"""


def f_to_c(f_temp):
    return (f_temp - 32) * 5 / 9


def c_to_f(c_temp):
    return (c_temp * 9 / 5) + 32


def temp_conversion(temp, units):
    if units == 1:
        c = f_to_c(temp)
        k = c + 273.15
        return temp,c,k

    elif units == 2:
        k = temp + 273.15
        f = c_to_f(temp)
        return f,temp,k

    else:
        c = temp - 273.15
        f = c_to_f(c)
        return f, c, temp
    # print(f'F = {f:.2f}, C = {c:.2f}, K = {k:.2f}')

print("For Temperature conversion, enter the temperature to be converted")
print("\tand the temperature units. For the units enter a 1 for F, 2 for C or 3 for Kelvin.")
temp_input = input("Enter temperature first, followed by units. eg (25 2) For 25 degrees C. ")

print(temp_input)

temp_in = temp_input.split(" ")

print(temp_input, " -- ", temp_in)

value_input = float(temp_in[0])
units_input = int(temp_in[1])
print(units_input)
print(value_input)


temp_return = temp_conversion(value_input,units_input)

print(f'\nF = {temp_return[0]:.4f}, C = {temp_return[1]:.4f}, K = {temp_return[2]:.4f}')