#!/usr/bin/python3
def uppercase(str):
    for y in str:
        if ord(y) in range(97, 123):
            i = ord(y) - 32
        else:
            i = ord(y)
        print("{:c}".format(i), end='')
    print("")
