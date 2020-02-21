"""Solve each of the following problems using Python Scripts. Make sure you use appropriate variable names and
comments. When there is a final answer have Python print it to the screen.A person’s body mass index (BMI) is
 defined as: BMI=mass in kg / (height in m)2."""

Height=int(input('Enter the value of Height'))
Weight=int(input('Enter the value of Weight'))
BMI=Weight/Height*Height
print(BMI)