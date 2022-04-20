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

#
# Define functions
#
''' Python program to print all primes smaller than or equal to
 n using Sieve of Eratosthenes'''


def sieve_of_eratosthenes(n):
    """ Python program to print all primes smaller than or equal to
     n using Sieve of Eratosthenes"""


    """
    Create a boolean array "prime[0..n]" and initialize
    all entries it as true. A value in prime[i] will
    finally be false if i is Not a prime, else true.
    """
    prime = [True for i in range(n + 1)]
    counter = 0
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            print(p, end=' ')  # Use print(p) for python 3
            counter += 1
    print(f"\n\nThere are {counter} prime numbers in this list.")




# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":
    clear()
    print()

    # driver program
    if __name__ == '__main__':
        n = get_data("i", "Enter an integer. ")

        print(f"\nFollowing are the prime numbers smaller", end=' '\
              f"than or equal to {n}. \n")
        sieve_of_eratosthenes(n)

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
