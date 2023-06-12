#!/usr/bin/python3

def no_c(my_string):
    new_string = ''
    for word in my_string:
        if word != 'c' and word != 'C':
            new_string = new_string + word
    return (new_string)
