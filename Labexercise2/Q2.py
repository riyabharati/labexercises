"""WAP which accepts marks of four subjects and display total marks, percentage and
grade.
Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass,
less than 40% –> fail"""

M=int(input('Enter the Marks in Mathematics'))
N=int(input('Enter the Marks in Nepali'))
S=int(input('Enter the Marks in Social'))
P=int(input('Enter the Marks in Physics'))

t=M+N+S+P
per=(t/400)*100
print('The Total Marks is',t)
if per>80:
    print('Distinction ')
    print('A+')
elif per>60<80:
    print('First Division')
    print('A')
elif per>50<60:
    print('Second Division')
    print('B+')
else:
    print('Fail')

