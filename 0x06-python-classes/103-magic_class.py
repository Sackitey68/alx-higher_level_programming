#!/usr/bin/python3
"""Defines a class Magic_class"""
import math


class MagicClass:
    """This represents a circle"""
    def __init__(self, radius=0):
        """Initializes the magic_class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Circumference of the circle"""
        return 2 * math.pi * self.__radius
