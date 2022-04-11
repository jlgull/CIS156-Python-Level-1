#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
import json


#
# Define functions
#

array = '{"fruits": ["apple", "banana", "orange"]}'
        #' "stuff": ["toys", "candy", "shoes"]}'

data = json.loads(array)

print(data,"\n")

for k in data:
    print(k)
# the print displays:
# [u'apple', u'banana', u'orange']

# End of Program
