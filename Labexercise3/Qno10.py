"""Write a program to find the factorial of a number using functions"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input('enter the number'))
print(factorial)
