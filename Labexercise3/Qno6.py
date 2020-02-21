"""Write a Python program to reverse a string."""

def revstr(string):
    rev = ""
    for i in range(len(string) - 1, -1, -1):
        rev = rev + string[i]
    print(f"Reverse of '{string}' is '{rev}'")
    print()
revstr(string)
