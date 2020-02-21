"""Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as
forward, e.g., madam or nurses run"""


def isPalindrome(inS):
    S = inS.lower()
    if len(S) == 1 or len(S) == 0:
        return True
    if S[0] == S[-1]:
        middle = S[1: -1]
        return isPalindrome(middle)
    else:
        return False
