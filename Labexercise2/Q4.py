"""Given three integers, print the smallest one. (Three integers should be user input)"""

Num1=int(input('Enter the Number:'))
Num2=int(input('Enter the Number:'))
Num3=int(input('Enter the Number:'))
if Num1<Num2<Num3:
    print('Num1 is Smallest One ')
elif Num2<Num1<Num3:
    print('Num2 is Smallest One')
else:
    print('Num3 is Smallest')