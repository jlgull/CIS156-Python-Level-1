#! / bin / python3
#
# Author: Jonathan Heard
# Instructor: Tim McMichael
# Course: CIS156, Section 36323
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# Program name: phone_service.py
#
"""

Ch 4 Programming Assignment, Part A

EMobile Phones is a new provider of cellular phone service for students at EMCC. Write a program called
    phone_service.py to help customers choose a service plan.
    Prompt the user to input the following information:

    Maximum number of "talk" minutes
    Maximum number of SMS/text messages
    Maximum amount of data, in gigabytes.

Based on the input, use branching to recommend appropriate service plan options:

    A customer who needs fewer than 500 minutes of talk and no text or data should accept
        Plan A at $49 per month.
    A customer who needs fewer than 500 minutes of talk and any text messages--but no data--should accept
        Plan B at $55 per month.
    A customer who needs 500 or more minutes of talk and no data should accept either
        Plan C for up to 100 text messages at $61 per month or
        Plan D for 100 text messages or more at $70 per month.
    A customer who needs any data should accept
        Plan E for up to 3 gigabytes at $79 or Plan F for 3 gigabytes or more at $87.
"""

"""
Variable List

talk_minutes    - holds the number of minute the customer estimates they need
text_messages   - holds the number of text messages the customer estimates they need
data_gbytes     - holds the number of gigabytes of data the customer estimates they need

service_plans   - dictionary variable hold the various plans and their costs
plan            - holds the plan selected by the program for the user
  
"""

# Fill the service_plans variable with the various plan options
#   Plan name followed by the month cost, in dollars.
#   If there are changes to plan costs in the future, only
#       the service_plans assignment will need to be changed,
#       there will be no need to review the entire code package.

service_plans = {
    "A": 49, "B": 55, "C": 61, "D": 70, "E": 79, "F": 87
    }

# Test print of the service plan information.
# print(service_plans)

# Prompt the user to input the following information:
#
#     Maximum number of "talk" minutes
#     Maximum number of SMS/text messages
#     Maximum amount of data, in gigabytes.

print("\nWelcome to the EMobile Phones plan selection tool.")
print("\nBased on your answers to a few simple question,")
print("\tan appropriate plan will be suggested.")

talk_minutes = int(input("\nFirst, enter your estimated number of talk minutes per month: "))
text_messages = int(input("\nSecond, enter your estimated number of text messages per month: "))
data_gbytes =   int(input("\nFinally, your estimated data usage in GB (gigabytes) per month: "))

# Display the data entered

print("\nYou entered", talk_minutes, "as estimated talk minutes.")
print("You entered", text_messages, "as estimated text messages.")
print("You entered", data_gbytes, "as estimated data usage, in GBs.")

"""
Based on the input, use branching to recommend appropriate service plan options:
   A customer who needs fewer than 500 minutes of talk and no text or data should accept
        Plan A at $49 per month.
   A customer who needs fewer than 500 minutes of talk and any text messages--but no data--should accept
        Plan B at $55 per month.
   A customer who needs 500 or more minutes of talk and no data should accept either
        Plan C for up to 100 text messages at $61 per month or
        Plan D for 100 text messages or more at $70 per month.
   A customer who needs any data should accept
        Plan E for up to 3 gigabytes at $79 or Plan F for 3 gigabytes or more at $87.
"""

# Logic section to, select the appropriate plan, based on the data collected.
# Test for data first, then minutes and finally messages.
#   Using ternary operations to reduce the lines of code.

if data_gbytes == 0:
        if talk_minutes < 500:
            plan = "B" if (text_messages > 0) else "A"
        else:
            plan = "D" if (text_messages >= 100) else "C"
else:
    plan = "E" if (data_gbytes < 3) else "F"

# Print out the suggested plan

print("\nThe suggested plan for you is Plan", plan, "which cost $", service_plans[plan], "per month.")

# End of program
