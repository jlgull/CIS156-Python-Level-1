#!/bin/python3
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

# Lebron James: Statistics for 2003/2004 - 2012/2013
years_played = ['2003/2004', '2004/2005', '2005/2006',
                '2006/2007', '2007/2008', '2008/2009',
                '2009/2010', '2010/2011', '2011/2012',
                '2012/2013']
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

print(f"Total Points: {sum(points)}")  # Print total points

# Print Average PPG
print(f"Average PPG: {(sum(points[:]) / sum(games_played)):.3f}")

# Print best scoring years (Ex: 2004/2005)

for i in range(len(points)):
    if max(points) == points[i]:
        print(f"Best Scoring years: {years_played[i]}, with {points[i]} points.")

# Print worst scoring years (Ex: 2004/2005)
for i in range(len(points)):
    if min(points) == points[i]:
        print(f"Worst Scoring years: {years_played[i]}, with {points[i]} points.")


user_input = input()
hourly_temperature = user_input.split()

for i in range(len(hourly_temperature)):
    print(hourly_temperature[i], end=" -> " if i != len(hourly_temperature)-1 else " \n")


# End of Program
