"""Write a function called fizz_buzz that takes a number. If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”. If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number."""

def fizz_buzz(a):
    rem3 = a % 3
    rem5 = a % 5
    if rem3 == 0 and rem5 == 1:
        t = "Fizz"
    elif rem3 == 1 and rem5 == 0:
        t = "Buzz"
    elif rem3 == 0 and rem5 == 0:
        t = "FizzBuzz"
    else:
        t = a
    print()
    return t

a = int(input('Enter the Number:'))
fizz_buzz(a)