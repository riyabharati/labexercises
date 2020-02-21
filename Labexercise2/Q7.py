"""Given a positive real number, print its fractional part. """

print("Enter a Number")
Num = float(input())

strb = str(Num)                                  # seperating into integer and decimal values

temp = strb.split(".")                        # spliting num and interval in list format eg: 23.54 = [23, 54] as string

# value after decimal point
decimal = int(temp[1])                         # value of decimal as integer
power = 10 ** (len(str(decimal)))               # power multiple of 10^length of decimal, also denominator
div = 2                                           # common divisor for numerator and denominator
tempn = Num * power
tempm = power

# loop to convert to smallest fraction
while not div == 6:
    if (tempn / div) == (tempn // div) and (tempm / div) == (tempm // div):
        tempn = tempn / div
        tempm = tempm / div
    else:
        div += 1
print(f"Fraction form: {int(tempn)}/{int(tempm)}")
print()
