#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: payroll.py
#
"""

Ch 4 Programming Assignment, Part B

Renee's Rad Restaurant pays employees differently depending on their job title and experience.
    In a program called payroll.py, use separate prompts to collect the following input:

    Job title ("W" for wait staff, "H" for host, "K" for kitchen staff)
    Number of hours worked
    Number of years employed at the restaurant

Then, output their gross pay amount (i.e., the amount they earn before taxes and other deductions)
    based on the following:

    Wait staff earns $5/hour until they've worked 1 year, then earn $6/hour
    Hosts earn $12/hour for the first 2 years, then go up to $13.50/hour
    Kitchen staff make $15/hour for the first year, then go to $18/hour

Note: At this stage, you do not need to worry about "rounding off" the numbers to look like currency.
    It's okay if they have an incorrect number of decimal places.

"""

"""
Variable List

String variables:
job     - which job ("W" for wait staff, "H" for host, "K" for kitchen staff)
job_title_dic   - dictionary list of job titles to simple character label, both key and data are strings
employee_first_name - employee's first name only

Floating point numbers:
hours_worked    - hours worked in the last week
wage_rate       - hourly rate, based on job and years employed

Integers numbers: 
years_employed  - number of years employed in the current position

"""

# Create and fill the job_title_dic with defining information

job_title_dic = {
        "W": "wait staff",
        "H": "host",
        "K": "kitchen staff"
    }

# Gather required data to determine gross pay

print("\nWelcome to the Renee's Rad Restaurant payroll system.")

employee_first_name = input("\nPlease enter your first name: ")

# Get the number of years the employee has been in the current position

years_employed = int(input("Please enter the number of years you have been with us: "))

# Use a while loop to verify that only a valid job title code is entered

while True:
    print("\n", employee_first_name, ", please enter your job title code, based on the following list.")
    print('\t"W" for wait staff, "H" for host, "K" for kitchen staff')
    job = input("\tEnter the job title code: ")
    job = job.capitalize()

# Test for valid job title code

    if (job == "W") or (job == "H") or (job == "K"):
        break

    print("Please enter a valid code: W, H or K")

# Use a while loop to verify that only a valid number of hours worked is entered
while True:
    hours_worked = float(input("\nPlease enter your the number of hours you worked last week: "))

# Test for valid hours worked data

    if (hours_worked > 0.0) and (hours_worked <= 40.0):
        break

    print("Please re-enter your work hours, if you worked more than 40 hours you will")
    print("\tneed your supervisors approval for the overtime.")

# All the data required to calculate the gross pay have been entered.
#   Now a decision tree will be used to arrive at the correct hourly rate
#
#       Wait staff earns $5/hour until they've worked 1 year, then earn $6/hour
#       Hosts earn $12/hour for the first 2 years, then go up to $13.50/hour
#       Kitchen staff make $15/hour for the first year, then go to $18/hour
#
#       Using ternary operations to reduce the lines of code.
#
# Set wage rate for Wait Staff

if job == "W":
    wage_rate = 6.0 if (years_employed > 1) else 5.0

# Set wage rate for Host

elif job == "H":
    wage_rate = 13.5 if (years_employed > 2) else 12

# Set wage rate for Kitchen Staff, no test is required since only 3 job
#   codes are allowed in the entry section.

else:
    wage_rate = 18 if (years_employed > 1) else 15

# Print out the information gathered and the gross pay calculation

print("\n", employee_first_name, "your entered job code was", job, "which is for", job_title_dic[job], ".")
print("\tYou have worked here", years_employed, f"years and last week you worked {hours_worked:.2f} hours.")
print(f"\tYour hourly wage rate is ${wage_rate:.2f} and your gross pay is ${hours_worked * wage_rate:.2f}")


# End of program
