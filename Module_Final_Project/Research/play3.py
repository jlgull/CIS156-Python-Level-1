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

lst = ['Hello', ' there', ' world!']

print(lst)

with open('example.json', 'w') as f:
    json.dump(lst, f)

with open('example.json') as f:
  data = json.load(f)

print(type(data))

# lst = data.split()

words = []

for i in range(len(data)):
    words.append(data[i])

print(words)

# End of Program
