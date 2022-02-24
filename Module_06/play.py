#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
def my_function(n):
    print(f"Hello from a function, {n}")


def my_function_many(n):
    for i in range(1, n+1):
        my_function(i)

my_function_many(10)

