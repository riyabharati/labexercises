"""Write a Python program to guess a number between 1 to 9. Note : User is prompted to enter a guess. If the user
guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a
"Well guessed!" message, and the program will exit"""


import random

num = random.randrange(10)
ans = 11
while ans != num:
    print("Enter your guessed number")
    ans = int(input())
print("Well Guessed!")