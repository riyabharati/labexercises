""" Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters."""

# '''def calcase():
#     print("Enter the string to find no. of upper and lower case characters: ")
#     string = input()
#     upcnt = 0
#     lowcnt = 0
#     for i in range(len(string)):
#         if string[i].isupper():
#             upcnt += 1
#         elif string[i].islower():
#             lowcnt += 1
#     print(f"There are {upcnt} upper-case characters.")
#     print(f"There are {lowcnt} lower-case characters.")
#     print()'''
#
# """ accepts a string and calculate the number of upper case letters and lower case letters"""


def calcase():
    print("Enter the string to find no. of upper and lower case characters: ")
    string = input()
    upcnt = 0
    lowcnt = 0
    for i in range(len(string)):
        if string[i].isupper():
            upcnt += 1
        elif string[i].islower():
            lowcnt += 1
    print(f"There are {upcnt} upper-case characters.")
    print(f"There are {lowcnt} lower-case characters.")
    print()


calcase()
