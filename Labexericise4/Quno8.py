"""Write a Python program to get the Fibonacci series between 0 to 50. Note : The Fibonacci Sequence is the
 series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....   Every next number is found by adding up the two numbers
before it """

# display the Fibonacci series between 0 and 50
display = 0
a = 1
series = []
while display <= 50:
    series.append(display)
    temp = display
    display = display + a
    a = temp
print(series)