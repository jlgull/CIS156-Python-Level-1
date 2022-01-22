#! / bin / python3
#
# Author: Jonathan Heard
# Work for CIS156, Spring 2022, based on zyBook, CIS156: Python Programming: Level 1
#
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# 1) Program taken from Python For Everybody (PFE), Chapter 1, Page 11

# Get the name of the file to count the words in.
#
name = input('Enter a file name: ')
handle = open(name, 'r')

# Preset variable

counts = dict()
bigcount =  None
bigword =   None

# Loop to count words in each line of the file

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# After each line, set bigcount variables

for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print('Most common word:',bigword, ', and # of occurances:', bigcount)




