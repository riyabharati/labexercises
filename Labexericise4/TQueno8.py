"""Write a Python program to create the colon of a tuple."""

from copy import deepcopy

# create a tuple
tupleg = ("HELLO", 5, [], True)
print(tupleg)
# make a copy of a tuple using deepcopy() function
tupleg_colon = deepcopy(tupleg)
tupleg_colon[2].append(50)
print(tupleg_colon)
print(tupleg)
