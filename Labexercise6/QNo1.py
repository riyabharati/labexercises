"""Write a Python program to find out the sum of element of a list by using recursion."""


total = 0
num = 0

# creating a list
list1 = [98, 67, 41, 65, 95]


while (num < len(list1)):
    total = total + list1[num]
    num += 1

print("Sum of all elements in given list: ", total)
