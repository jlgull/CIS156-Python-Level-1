#! / bin / python3
#
# Author: Jonathan Heard
# Work for CIS156, Spring 2022, based on zyBook, CIS156: Python Programming: Level 1
#
# This is a sample Python script, built to follow along with conditional video.

"""

Create a program to prompt user to choose motel bedroom details, beds and view,
    in order to determine daily rate. Then ask about the number of days,
    then calculate the cost of the stay.

"""

""" 
variable list,
    room_rate_dic   - dictionary to hold rate information
    room_size_dic   - dictionary to hold type of room information
    room_view_dic   - dictionary to hold room view information
    room_size   - what type of room, to pick room_rate
    room_rate   - nightly rate
    view_choice - lake view or park view
    num_nights  - how many nights will the stay be

"""
# Define room rate dictionary

room_rate_dic = {1: 110, 2: 119, 3: 129}

# Define room rate dictionary

room_size_dic = {1: "Queen Bed",
                 2: "King Bed",
                 3: "King Bed with pullout Sofa"}

# Define room rate dictionary

room_view_dic = {1: "Lake View",
                 2: "Park View"}

# Find out the desired room type

while True:
    print("\nPlease select room type:")
    print("\t1 for Queen Bed")
    print("\t2 for King Bed")
    print("\t3 for King Bed and a pullout sofa")
    room_size = int(input("\nRoom Type Choice: "))
    if (room_size == 1) or (room_size == 2) or (room_size == 3):
        break
    else:
        print("Please make a valid choice: 1, 2 or 3!")

# Find the view, 1 = Lake view or 2 = park view.

while True:
    print("\nPlease view room:")
    print("\t1 for Lake View")
    print("\t2 for Park View")
    view_choice = int(input("\nRoom View Choice: "))
    if (view_choice == 1) or (view_choice == 2):
        break
    else:
        print("Please make a valid choice: 1 or 2!")

# Find out how many nights the stay will be

num_nights = int(input("\nHow many nights will the stay be? "))

# Determine the base nightly rate

room_rate = room_rate_dic[room_size]

# Modify the nightly rate for the Lake view.

room_rate = room_rate if (view_choice == 2) else room_rate + 20

print(f"\n\nThe total stay will cost $ {room_rate * num_nights:.2f}.")
print("\tThis is for a", room_size_dic[room_size], "and the", room_view_dic[view_choice], ".")
print(f"\tYour nightly rate is $ {room_rate:.2f}.")


# End of Program

