# Python program to demonstrate
# Conversion of JSON data to
# dictionary


# importing the module

from kennedy_13 import clear

from baby_boy_names import *

from baby_girl_names import *

clear()

print(f"There are {len(boys_list)} name in the boys list.")


print(f"There are {len(girls_list)} name in the girls list.")

all_names = boys_list + girls_list

all_names_copy = all_names[:]

all_names_copy.sort()

print(f"There are {len(all_names_copy)} name in the combined list.")

for i in range(0, 2000, 100):
    print(i, all_names_copy[i])



# Print the data of dictionary




