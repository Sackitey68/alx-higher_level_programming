#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNumber = abs(number) % 10
if number < 0:
    lastNumber = -lastNumber
print("Last digit of {} is {} and is ".format(number, lastNumber), end="")
if lastNumber > 5:
    print("greater than 5")
elif lastNumber == 0:
    print("0")
else:
    print("less than 6 and not 0")
