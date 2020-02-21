"""For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’
if it is 0."""

x = int(input("Enter a Number: "))
if x > 0:
    print('Positive')
elif x<0:
    print('Negative')
else:
    print('Zero')