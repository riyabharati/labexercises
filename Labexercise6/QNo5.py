"""Write a recursive program to check if the number is palindrome or not"""



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