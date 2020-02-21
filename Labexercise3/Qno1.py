""" Write a Python function to find the Max of three numbers"""

def Maximum(a, b, c):
    if a >= b and a >= c:
        num = a
    elif b >= a and b >= c:
        num = b
    else:
        num = c
    print("Maximum Number is ", num)


a = int(input('Enter the Number:'))
b = int(input('Enter the Number:'))
c = int(input('Enter the Number:'))
Maximum(a,b,c)