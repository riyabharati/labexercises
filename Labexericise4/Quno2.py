"""Write a Python program to convert temperatures to and from celsius, fahrenheit. C = (5/9) * (F - 32)"""

print("Choose the conversion: ")
print("    [c] for celsius to fahrenheit")
print("    [f] for fahrenheit to celsius")
ans = input()
conv = 0
cs = ""
if ans == "c":
    ans = "Celsius"
elif ans == "f":
    ans = "Fahrenheit"
print(f"Enter your temperature in {ans}")
temp = int(input())
if ans == "Celsius":
    conv = temp * (9 / 5) + 32
    cs = "Fahrenheit"
elif ans == "Fahrenheit":
    conv = (5 / 9) * (temp - 32)
cs = "Celsius"
print(f"{temp} ({ans}) is {conv} ({cs})")
print()