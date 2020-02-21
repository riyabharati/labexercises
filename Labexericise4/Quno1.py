"""Write a Python program to find those numbers which are divisible by 7 and  multiple of 5, between 1500 and 2700
 (both included)."""

print()
Num = []
for i in range(1500, 2700 + 1):
    if i % 7 == 0 and i % 5 == 0:
        Num.append(i)
print(f" The Numbers between 1500 and 2700 that are divisible by both 7 and 5 are:")
print(Num)
print()
