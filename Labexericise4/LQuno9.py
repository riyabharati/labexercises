"""Write a Python program to select an item randomly from a list."""

# initializing list
import random

test_list = [1, 4, 5, 2, 7]

# printing original list
print ("Original list is : " + str(test_list))

# using random.choice() to
# get a random number
random_num = random.choice(test_list)

# printing random number
print ("Random selected number is : " + str(random_num))
