"""Write a Python program that accepts a string and calculate the number of digits and letters"""

print("Enter the string:")
ans = input()
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "num", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z"]
digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
numlet, numdig = 0, 0
for i in ans:
    if i in letters:
        numlet += 1
    elif i in digits:
        numdig += 1
print(f"{numdig} letters, {numlet} digits")
