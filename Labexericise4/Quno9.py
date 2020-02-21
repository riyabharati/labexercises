"""Write a program to find the factorial of a number"""


# """find factorial of a number"""
factorial = []
num = int(input("Enter the num to find its factorial: "))
for i in range(1, num):
    if num % i == 0:
        factorial.append(i)
print(f"The factorials of {num} are {factorial}")
print()
