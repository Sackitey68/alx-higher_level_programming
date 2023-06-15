#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key, i in list(a_dictionary.items()):
        if i == value:
            del a_dictionary[key]
    return a_dictionary
