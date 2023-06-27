#!/usr/bin/python3
"""This class defines a square."""


class Square:
    """
    Private instance attribute: size

    Arttribute:
        size (int): size of the square (private)
    """

    def __init__(self, size=0):
        """
        Square instance initialisation

        Args:
            size (int): this is size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This defines a public instance method"""
        return self.__size * self.__size
