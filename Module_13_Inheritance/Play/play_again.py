#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#

#
# Define functions
#
clothing = list()

class InventoryTag:
    def __init__(self):
        self.object = ""
        self.item_id = 0
        self.quantity_remaining = 0

sweater = InventoryTag()
print("sweater", type(sweater))
# print("sweater", sweater[0])

clothing.append(sweater)
counter = len(clothing) - 1
print(clothing[counter])
clothing[counter].item_id = int(input("Enter ID number: "))
clothing[counter].quantity_remaining = int(input("Number remaining? "))

coat = InventoryTag()
clothing.append(coat)
counter = len(clothing) - 1

clothing[counter].item_id = int(input("Enter ID number: "))
clothing[counter].quantity_remaining = int(input("Number remaining? "))


for i in range(len(clothing)):
    print(f"ID item {i}: {clothing[i].item_id}")
    print(f"Qty {i}: {clothing[i].quantity_remaining}")


# End of program
