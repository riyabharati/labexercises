"""Write a Python program that accepts a word from the user and reverse it."""

# accepts a word from user and reverses it
print("Enter the word to be reversed")
word = input()
rev = ""
for i in word:
    rev = i + rev
print(rev)