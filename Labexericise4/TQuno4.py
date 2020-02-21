"""Write a Python program to unpack a tuple in several variables."""

# create a tuple
t = 4, 8, 3
print(t)
n1, n2, n3 = t
# unpack a tuple in variables
print(n1 + n2 + n3)
# the number of variables must be equal to the number of items of the tuple
n1, n2, n3, = t
