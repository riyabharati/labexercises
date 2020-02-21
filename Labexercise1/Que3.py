"""N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains
in the basket. How many apples will each single student get? How many apples will remain in the basket? The program
reads the numbers N and K. It should print the two answers for the questions above."""

N = int(input("Number of Students: "))
K = int(input("Number of Apples: "))
# after distributing them evenly
remain = K % N
each = K // N
print('The remaining Apples is',remain)
print('Each Apples Students get',each)
