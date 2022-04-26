#!/bin/python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
from kennedy_13 import clear, get_data
""" This is a module written to contain tools used throughout the main program
        to reduce the duplication of code as the designed moved forward.
        clear() - Performs a screen clear using the OS module and is intended to by Operating System (OS)
                    independent or agnostic.
        get_data    - Is used for all data entry requests. It used try/except to ensure that the data
                        entered is the type expected and it also expects a clarifying question or statement. 
"""

from time import perf_counter
"""
Found a reference on this website: https://realpython.com/python-timer/
"""


#
# Define functions
#
''' Python program to print all primes smaller than or equal to
     n using Sieve of Eratosthenes'''


def sieve_of_eratosthenes(lower_limit, upper_limit):
    """ Python program to print all primes smaller than or equal to
     n using """

    """
    Create a boolean array "prime[0..n]" and initialize
    all entries it as true. A value in prime[i] will
    finally be false if i is Not a prime, else true.
    """

    tic = perf_counter()

    prime = [True for i in range( upper_limit + 1)]
    counter = 0
    p = 2
    while p * p <= upper_limit:

        # If prime[p] is not changed, then it is a prime
        if prime[p]:

            # Update all multiples of p
            for i in range(p ** 2, upper_limit + 1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    for p in range(upper_limit + 1):
        if prime[p] and p >= lower_limit:
            print(p, end=', ')  # Use print(p) for python 3
            counter += 1

    toc = perf_counter()

    print(f"\nRun time is {toc - tic:0.4f} Seconds")
    print(f"\n\nThere are {counter} prime numbers in this list.")


# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":
    clear()
    print()

    # driver program
    if __name__ == '__main__':
        print(f"\nThis program will find all the prime numbers between the two (2) numbers you enter.")

        lower_limit = get_data("i", "Enter lower limiting integer now: ")
        upper_limit = get_data("i", "Enter upper limiting integer now: ")

        print(f"\nFollowing are the prime numbers between {lower_limit } and {upper_limit}. \n")

        sieve_of_eratosthenes(lower_limit, upper_limit)

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to run this again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of Program
