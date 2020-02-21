"""Write a Python program to print a specified list after removing the 0th, 4th and 5th elements"""

numlist = [1, 0, 8, 7, 6, 4, 9]
listb = numlist.copy()
del listb[0]
del listb[4 - 1]  # accounting for 1 item already removed
del listb[5 - 2]  # accounting for 2 items already removed
print(listb)
print()
