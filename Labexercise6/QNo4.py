""" Write a recursive function that check if the given string is palindrome, else not palindrome."""


def palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String is not a palindrome!")