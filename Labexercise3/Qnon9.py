""" Accept string from the user and display only those characters which are present at an even index"""

def evenindx(string):
    print(f"The characters in the even index of {string}are: ")
    for i in range(0, len(string) + 1, 2):
        print(string[i])
    print()

string=input('enter the string')