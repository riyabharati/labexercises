""" Write a Python program to convert a tuple to a string."""


def convertTuple(tup):
    str = ''.join(tup)
    return str


# Driver code
tuple = ('g', 'e', 'e', 'k', 's')
str = convertTuple(tuple)
print(str)