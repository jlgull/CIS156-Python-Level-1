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
    print(f"i_c = {i_c}, ii_c = {ii_c}, v_c = {v_c}, x_c = {x_c}, xx_c = {xx_c}, l_c = {l_c}, c_c = {c_c}")
    print(f"Total $ {i_c + ii_c*2 + v_c*5 + x_c*10 + xx_c*20 + l_c*50 + c_c*100}")
    return i_c + ii_c*2 + v_c*5 + x_c*10 + xx_c*20 + l_c*50 + c_c*100


print("Enter number of bills, by denomination as asked.")
i_count = int(input("Number of ones in your wallet: "))
ii_count = int(input("Number of twos in your wallet: "))
v_count = int(input("Number of fives in your wallet: "))
x_count = int(input("Number of tens in your wallet: "))
xx_count = int(input("Number of twenties in your wallet: "))
l_count = int(input("Number of fifties in your wallet: "))
c_count = int(input("Number of hundreds in your wallet: "))

total_cash = count_bills(i_c=i_count, ii_c=ii_count,v_c=v_count,
                         x_c=l_count, xx_c=xx_count, l_c=l_count, c_c=c_count)

print(f"The total of your wallet cash is $ {total_cash}")
