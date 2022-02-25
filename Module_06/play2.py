#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

def count_bills(i_c=0, ii_c=0, v_c=0, x_c=0, xx_c=0, l_c=0, c_c=0):
    global bill_array
    total_cash = 0
    # print(f"i_c = {i_c}, ii_c = {ii_c}, v_c = {v_c}, x_c = {x_c}, xx_c = {xx_c}, l_c = {l_c}, c_c = {c_c}")
    # print(f"Total $ {i_c + ii_c*2 + v_c*5 + x_c*10 + xx_c*20 + l_c*50 + c_c*100}")
    for t in range(0,len(bill_array), 3):
         total_cash = total_cash + (bill_array[t + 1] * bill_array[t + 2])
    return total_cash

bill_array = ['Ones', 1, 'i_count',
              'Twos', 2, 'ii_count',
              'Fives', 5, 'v_count',
              'Tens', 10, 'x_count',
              'Twenties', 20, 'xx_count',
              'Fifties', 50, 'l_count',
              'Hundreds', 100, 'c_count',]

for i in range(0,len(bill_array), 3):
    while True:
        print(f"Please enter the number of ${bill_array[i + 1]} bills in your wallet: ", end='')
        input_number = input()
        if ('0' <= input_number <= '9'):
            bill_array[i + 2] = int(input_number)
            break
        print("The entry must be a number between 0 and 9.\n")

# For testing of return the creation of the bill array.
# print(bill_array)

total_cash = count_bills(i_c=bill_array[2], ii_c=bill_array[5],
                         v_c=bill_array[8],x_c=bill_array[11],
                         xx_c=bill_array[14], l_c=bill_array[17],
                         c_c=bill_array[20])

print("\nIn your wallet you reported you have:")
for i in range(0,len(bill_array), 3):
    if bill_array[i+2] == 1:
        print(f"    {bill_array[i + 2]} - ${bill_array[i + 1]} bill")
    else:
        print(f"    {bill_array[i+2]} - ${bill_array[i + 1]} bills")

print(f"\nThis totals to ${total_cash} cash in your wallet.")

