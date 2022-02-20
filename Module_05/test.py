#!/bin/python3

# Program from Tracy Baker, after we proved the printing of the Histogram

import random
dice = {}

rolls = int(input('How many rolls? '))

for i in range(2,13):
    dice[i] = 0

for i in range(rolls):
#    total = (random.randint(1,6)) + (random.randint(1,6))
    dice[(random.randint(1,6)) + (random.randint(1,6))] += 1

for i in range(2,13):
        print(f'{i}s\t', '%' * dice[i])
