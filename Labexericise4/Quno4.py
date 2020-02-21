"""Write a Python program to construct the following pattern, using a nested for
loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*        """




# make a right-pointed isoceles triangle pattern with maximum no. of * being 5
for i in range(1, 5 + 1):
    for j in range(i):
        print("*", end="")
    print()
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()