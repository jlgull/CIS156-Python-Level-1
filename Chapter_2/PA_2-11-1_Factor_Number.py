#! / bin / python3
#
# Author: Jonathan Heard
# Work for CIS156, Spring 2022, based on zyBook, CIS156: Python Programming: Level 1
#
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Program taken from zyBook, Chapter 2, This was created to find
#   where the numbers came from for the Numbers game

# Set the list variable for the factors to 0

factor = []

# Enter a large number to find its factors, those numbers which if multiplied together
#   would recreate the large number entered.

base_num = large_num = int(input('Enter a number to be factored:\n'))

for i in range(2, large_num):
    if large_num % i == 0 and i not in factor:
        factor.append(i)
        large_num = int(large_num / i)
        if large_num == 1:
            break

print('The factors for', base_num, 'are: ', *factor, sep='\t')




#result = num * (3 * 7 * 13 * 37)

#print(result)

#num = int(input('Enter 3 digit number:\n'))

#result = num * (7 * 11 * 13)

#print(result)

#num = int(input('Enter 5 digit number:\n'))

#result = num * (11 * 9091)

#print(result)

