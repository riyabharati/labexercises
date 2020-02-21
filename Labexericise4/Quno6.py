"""Write a Python program to count the number of even and odd numbers from a series of numbers."""

# count the number of even and odd numbers from a series of numbers

print("Enter the Series of Numbers: ")
num = input()
odd, even = 0, 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"The Number of odd Numbers is {odd}")
print(f"The Number of even Numbers is {even}")
