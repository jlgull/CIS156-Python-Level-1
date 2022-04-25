#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: pets.py
#
"""
Ch 13 Programming Assignment

Create a program called pets.py that that defines a pet class with at least three general
    attributes (fields) for all pets (for example, name, age, etc.) and at least two functions/behaviors
    for all pets (for example, eating). The functions can simply print something.

Next, create two derived classes from the base class that represent specific types of pets.
    For example, one derived class might be a dog. Add at least one attribute/field and at least
    two functions/behaviors specific to that kind of pet.

Finally, demonstrate that both derived classes work by creating at least one instance of each and
    showing off their fields and functions.

Note: In preparation for the Final Project, this assignment leaves room for you to make more
    decisions about the code than previous assignments. Just be sure that your submission demonstrates the key
    concepts from the chapter, as indicated in these directions.

"""
#
# Import all required options
#
# Import system and name from os

from kennedy_13 import clear, get_data
""" This is a module written to contain tools used throughout the main program
        to reduce the duplication of code as the designed moved forward.
        clear() - Performs a screen clear using the OS module and is intended to by Operating System (OS)
                    independent or agnostic.
        get_data    - Is used for all data entry requests. It uses try/except to ensure that the data
                        entered is the type expected and it also expects a clarifying question or statement. 
"""

from datetime import date

""" 
    This module will be used to deliver today's day when needed.
"""

from dateutil.relativedelta import *

"""
    This module will be used to calculate the age of the pet, when requested for 
    any print or display purposes.
"""

# End of import section


"""

Variable List

List info:
    pet_list        -   List variable to contain all the pets entered and allow for the
                            various methods to be applied to them.

String variables:
    In main program:
        do_again    -   Control value for repeating the program.
        command     -   The value entered into the menu system to control the main program.

    In class:
        gender_label    -   Used to create the appropriate he/she label for the pet being created.
        age_label       -   Used to select between "year" and "years" as appropriate.
                  
Floating point numbers:
    In main program:
  
    In function:

Integers numbers: 
    In main program:
      
    In function:
   
"""

#
# Class definition section of the program
#

"""
      Create a program called pets.py that that defines a pet class with at least three general
      attributes (fields) for all pets (for example, name, age, etc) and at least two functions/behaviors
      for all pets (for example, eating). The functions can simply print something.
"""


class Pet:
    """
    Define the Pet class, as each record is created the necessary data is collected.
    """
    def __init__(self, pet_type):
        self.type = pet_type
        self.name = get_data("s", f"Enter your {self.type}'s name. ")
        self.birth_day = date(int(input("Enter birth year: ")), int(input("Enter birth month: ")),
                              int(input("Enter birth day: ")))
        self.gender = get_data("s", "Is your pet, Male or Female? ").upper()

    def info_pet(self):
        """
        Create the print information for each pet created.
        """
        gender_label = "he" if self.gender.upper().startswith("M") else "she"
        print(f"Your {self.gender.lower()} {self.type.lower()}'s name is {self.name.title()}", end="")

        # Get today's date, so the pet's age can be calculated.
        today = date.today()

        # Determine the pet's age.
        pet_age = relativedelta(today, self.birth_day)

        # More examples at: https://www.plus2net.com/python/date-relativedelta.php

        # If the pet is only 1 year old, use the singular form of year.
        age_label = "year" if pet_age.years == 1 else "years"
        print(f" and {gender_label} is {pet_age.years} {age_label} old.")


"""
    Next, create two derived classes from the base class that represent specific types of pets.
        For example, one derived class might be a dog. Add at least one attribute/field and at least
        two functions/behaviors specific to that kind of pet.
"""


class Cat(Pet):
    def __init__(self):
        Pet.__init__(self, "Cat")
        self.speak = "Meeoow, Meeoow"
        self.hair_length = get_data("s", "Is your cat Short or Long haired? ")
        self.fav_food = get_data("s", "Does your cat prefer Canned or Dried cat food? ")

    def speak_cat(self):
        print(f"Your {self.type}, {self.name.title()}, says {self.speak}.")

    def info_cat(self):
        self.info_pet()
        print(f"In addition, {self.name.title()} is {self.hair_length.title()} haired and prefers "
              f"{self.fav_food.title()} food.")


class Dog(Pet):
    def __init__(self):
        Pet.__init__(self, "Dog")
        self.speak = "Woooff!, Woooff!!"
        self.breed = get_data("s", "What breed is your dog? ")
        self.color = get_data("s", "What color is your dog? ")

    def speak_dog(self):
        print(f"Your {self.type}, {self.name.title()}, says {self.speak}.")

    def info_dog(self):
        self.info_pet()
        print(f"In addition, {self.name.title()} is a {self.breed.title()} breed, "
              f"who is {self.color.title()}.")


# End of function definitions

# Set the while control value to "Y".
do_again = "Y"

pet_list = list()

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    clear()
    print()

    # Main body of the program.

    """
        Finally, demonstrate that both derived classes work by creating at least one instance of each and
            showing off their fields and functions.
    """

    print(f"This program gathers information about your pets, currently limited to just cats and dogs.\n"
          f" If requested, this program could be enhanced allow the pet list to be saved to a file\n"
          f" and then retrieved for expansion or modification. In addition other pet types, with the necessary\n"
          f" identifying information could be added.\n"
          f"Simply respond to the menu and answer the questions as they are presented.")

    menu = "\nBasic Menu,\n enter (c) to add a cat\n enter (d) to add a dog\n" \
           " enter (l) to list all your pets\n enter (s) for your pet to speak\n" \
           " or enter (q) to quit the program: "
    command = get_data("s", menu).lower()

    # Base menu used to create pet records and report out the data saved.
    while True:
        if command == "c":
            pet_list.append(Cat())
            break
        elif command == "d":
            pet_list.append(Dog())
            break
        elif command == "l":
            for pet in pet_list:
                if pet.type == "Cat":
                    print(pet.info_cat())
                else:
                    print(pet.info_dog())
            break
        elif command == "s":
            for pet in pet_list:
                if pet.type == "Cat":
                    print(pet.speak_cat())
                else:
                    print(pet.speak_dog())
            break
        elif command == "q":
            break
        else:
            print(f"\nYour choice \"{command}\" is Invalid, only c, d, l, s & q are valid!")
            break

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to run this program again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of program
