"""Given a three-digit number. Find the sum of its digits. """

print("Enter a Three- Digit Number")
a = int(input())

# separate number into digits
Num = str(a)
x = Num[0]
y = Num[1]
z = Num[2]
Sum = x + y + z
print('The Sum is ',Sum)
