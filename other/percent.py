# This program was written to play with math and to answer a question.
# The person wanted to know how to to subtract 75% from a value called current price
# I wrote the percent function then wrote a program using floats
# After writing this, I asked the question:
# Aren't floating point rounding errors dangerous for financial operations?
# I then proceeded to write the program again with only integers.

import re

def percent(base, percent):
    percent = percent / 100
    base = base * percent
    return base

def decIntPer(left, right, percent):
    percent = percent / 100
    left = left * percent
    right = right * percent
    right = right / 10
    output = left + right
    return output

userBase = input("Enter the base value: ")
userPercent = input("Enter the percent to subtract: ")

hasDecimal =  re.search("\.", userBase)
if hasDecimal:
    intDec = re.split("\.", userBase, 1)
    intDecLeft = int(intDec[0])
    intDecRight = int(intDec[1])
    userPercent = int(userPercent)
    userPercent = 100 - userPercent
    print(decIntPer(intDecLeft, intDecRight, userPercent))

    #print(intDec[0]+"."+intDec[1])
else:
    userBase = int(userBase)
    userPercent = int(userPercent)
    userPercent = 100 - userPercent
    print(percent(userBase, userPercent))
