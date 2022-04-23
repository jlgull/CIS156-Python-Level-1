#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: sum_loop.py
#
"""

Ch 5 Programming Assignment, Part A

Create a program called sum_loop.py. In it, ask the user for a starting number and an ending number.
Then use a loop (not a function) to calculate the sum of every number from the first to the second.
The image below shows an example of the user inputs 3 and 15.

"""

"""
Variable List

String variables:
play_again  - will collect the response for running the program again

Floating point numbers:

integer numbers: 
start_num   - number entered to start summing process
temp_start  - holds start, to be used if start is greater than end
end_num     - number entered to end summing process
temp_end    - holds end, to be used if start is greater than end
sum_total   - the total of the summing process

"""

# Introduction, to explain what the program does.

print("\n\nThis program will ask for 2 numbers and then sums them ")
print("\tfrom the starting number to the ending number.")
print("\tEither number can be negative and process will work.")
print("\n\tHere are some examples:")
print("\t\tWith 2 positive numbers, using the start as 1 and the end as 5, the sum is 15.")
print("\t\tWith 1 positive number and 1 negative number, using the start as -1 and the end as 5, the sum is 14.")
print("\t\tWith 2 negative numbers, using the start as -3 and the end as -1, the sum is -6.")

# Set up a while loop to allow for entry of additional pairs of numbers.

while True:

    # Ask the user for the starting and ending numbers, also capture the numbers
    #   in case the starting number is greater than the ending number.
    temp_start = start_num = int(input("\nPlease enter the starting number: "))
    temp_end = end_num = int(input("     Now enter the ending number: "))

    # If the starting number is greater than the ending number, switch the numbers.
    if temp_start > temp_end:
        end_num = temp_start
        start_num = temp_end

    # Summing total to 0, at the start of the calculation.
    sum_total = 0

    # Calculate the sum total.
    for x in range(start_num, end_num+1):
        sum_total += x

    # Message related to the starting number being greater than ending number.
    if temp_start > temp_end:
        print("\nThe starting number you entered was greater than the ending number.")
        print("\tBecause of this the two numbers were switch and the summation process")
        print("\t\twas performed with the switched pair of numbers.")
        print(f'\tYou entered {temp_start} as the start number and {temp_end} as the end number.')

    # Here is the printed output for the numbers entered.
    print(f'\nThe sum of all numbers from {start_num} to {end_num} is {sum_total}.')

    # Ask if the user would like to run the program again?
    # Also, validate for the correct response.
    while True:
        play_again = input("\n\nWould you like to run the program again? Enter (Y) for yes or (N) for no. ")
        play_again = play_again.upper()
        if play_again == "N" or play_again == "Y":
            break
        else:
            print("You need to enter either a Y or an N.")
    if play_again == "N":
        exit()


# End of program
