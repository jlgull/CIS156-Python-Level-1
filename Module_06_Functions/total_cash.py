#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: total_cash.py
#
"""

Ch 6 Programming Assignment, Part A

Create a program called total_cash.py that determines the total value of a wallet full of cash.
It should ask the user to input the quantity of each denomination of bills
    (ones, fives, etc--up to hundreds).
It should then call a function that accepts each of those values as arguments/parameters and
    returns (not prints!) the total amount of the cash.
Finally, you should output the total value for the user to see.

For example, if a user has 3 ones, 3 tens, and 1 fifty, their total is $83 in cash.

"""

"""
For the variables related to the bill denomination, I decided to use Roman Numerals for the 
    denominations. I for $1s, II for $2s, V for $5s, X for $10s, XX for $20, L for $50 and C for $100.
    This just allowed for simpler variable identification. The a "c" was added for use within the function.  

Variable List

Since there are no arrays in Python, so I used a list. Here is information about the (array) List.
List info:

    bill_array  -   is defined to hold several items related of the denominations in the wallet.
                    This is also being used as a global variable, both inside the function and the
                        main program.
                    There are 3 fields for each denomination.
                        The 1st field is the generic name for the denomination  - 'Ones'
                        The 2nd field is an integer, representing the value of the denomination  - 1
                        The 3rd field is an integer, representing the count of the denomination  -  'I_count'

String variables:
In main program (total_cash.py):
    do_again      -   will collect the response for running the program again
    input_string    - This is the raw, string value collected by input.
                    This value is tested to ensure it is a number and then converted
                    to an integer, if a number. If not a number a message is displayed
                    and a new request is made.

In function (count_bills):
                  
Floating point numbers:
In main program (total_cash.py):
  
In function (count_bills):

Integers numbers: 
In main program (total_cash.py):
    total_cash  -   The sum of the bills, based on data returned from the function.
      
In function (count_bills):
    cash_sum    -   The sum of the bills, calculated in the function and returned.  
   
"""

# Define the bill_array, which will be used throughout the program.
bill_array = ['Ones', 1, 'I_count',
              'Twos', 2, 'II_count',
              'Fives', 5, 'V_count',
              'Tens', 10, 'X_count',
              'Twenties', 20, 'XX_count',
              'Fifties', 50, 'L_count',
              'Hundreds', 100, 'C_count', ]

# Function definition section of the program

"""
It should then call a function that accepts each of those values as arguments/parameters and
    returns (not prints!) the total amount of the cash.

Here is the function to turn a count of the number of bills in your wallet or hand
   into a total cash amount. Since I only wanted to define the bill_array once, it was included
   as a global variable in the function.

 Determined I could use a global value, instead of passing the 7 different values. 
 # def count_bills(I_c=0, II_c=0, V_c=0, X_c=0, XX_c=0, L_c=0, C_c=0):
 """


def count_bills():
    # Use a global variable, so that it isn't necessary to pass
    #   data during the call of the program.
    global bill_array

    # Clear or set the total_cash variable.
    cash_sum = 0

    # Use a for loop to total the cash based on data entered in the calling program.
    for t in range(0, len(bill_array), 3):
        cash_sum = cash_sum + (bill_array[t + 1] * bill_array[t + 2])
    return cash_sum


# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Main body of the program.
    # It should ask the user to input the quantity of each denomination of bills
    #     (ones, fives, etc--up to hundreds).
    # Print a blank line between the data entered and the results.
    print("\n")

    # Use a for loop to collect how many of each bill denomination is to be summed.
    for i in range(0, len(bill_array), 3):
        while True:
            print(f"Please enter the number of ${bill_array[i + 1]} bills in your wallet: ", end='')
            input_string = input()

            # If the user enters nothing, the input value will be set to 0.
            if input_string == "":
                input_string = "0"

            # Test to ensure that a number between 0 and 9 was entered. The input was a string value; but
            #   only an integer is needed. This also prevents a none number entry from crashing the program.
            if '0' <= input_string <= '99':
                bill_array[i + 2] = int(input_string)
                break
            print("The entry must be a number between 0 and 99.\n")

    # Call the function, with the data that was entered.
    """
    This is how I first tried to pass the data to the function. Found I could use a global value
      to do the same thing. 
    total_cash = count_bills(I_c=bill_array[2], II_c=bill_array[5],
                             V_c=bill_array[8], X_c=bill_array[11],
                             XX_c=bill_array[14], L_c=bill_array[17],
                             C_c=bill_array[20])
    """

    total_cash = count_bills()

    # Print out the data supplied and the cash total, as well.
    # Don't print denomination when the user reported that they didn't have any of that denomination.
    print("\nIn your wallet you reported:")
    for i in range(0, len(bill_array), 3):
        if bill_array[i + 2] == 0:
            continue
        elif bill_array[i + 2] == 1:
            print(f"    {bill_array[i + 2]} - ${bill_array[i + 1]} bill")
        else:
            print(f"    {bill_array[i+2]} - ${bill_array[i + 1]} bills")

    print(f"\nThis totals to ${total_cash} cash in your wallet.")

    # The following code as copied from the sum_loop program.
    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to calculate the sum of your bills again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input()
        do_again = do_again.upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
