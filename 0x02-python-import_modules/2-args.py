#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argNum = len(argv)
    if argNum > 1:
        count = 0
        if argNum > 2:
            print("{:d} arguments:".format(argNum - 1))
        else:
            print("{:d} argument:".format(argNum - 1))
        for args in argv:
            count = count + 1
            if count != 1:
                print("{:d}: {}".format(count - 1, args))
    else:
        print("0 arguments.")
