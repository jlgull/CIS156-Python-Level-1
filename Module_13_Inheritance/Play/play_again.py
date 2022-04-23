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
        self.item_id = 0
        self.quantity_remaining = 0

sweater = InventoryTag()
print("sweater", type(sweater))
# print("sweater", sweater[0])

clothing.append(sweater)
print("clothing", type(clothing))

clothing[0].item_id = int(input())
clothing[0].quantity_remaining = int(input())

print(f"ID: {clothing[0].item_id}")
print(f"Qty: {clothing[0].quantity_remaining}")


# End of program
