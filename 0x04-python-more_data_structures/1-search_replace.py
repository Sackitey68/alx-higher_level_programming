#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [replace if z == search else z for z in my_list]
