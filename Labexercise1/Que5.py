"""A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students
in each class, print the smallest possible number of desks that can be purchased.The program should read three
integers: the number of students in each of the three classes, a, b and c respectively. In the first test there are
three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can
get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32
desks in total."""

a = int(input("Number of Students in Class A:"))
b = int(input("Number of Students in Class B:"))
c = int(input("Number of Students in Class C:"))
if (a % 2) == 0:
    D1 = int(a / 2)
elif (a % 2) == 1:
    D1 = int(a / 2) + 1
if (b % 2) == 0:
    D2 = int(b / 2)
elif (b % 2) == 1:
    D2 = int(b / 2) + 1
if (c % 2) == 0:
    D3 = int(c / 2)
elif (c % 2) == 1:
    D3 = int(c / 2) + 1
print("Total Number of benches needed is:", D1 + D2 + D3)
