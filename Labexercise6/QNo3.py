""" Write a recursive Python function that returns the sum of first n integers."""


def sumdigits(number):
  if number==0:
    return 0
  if number!=0:
    return (number%10) + (number//10)


def main():
    number=int(input("Enter a number :"))
    print(sumdigits(number))
main()