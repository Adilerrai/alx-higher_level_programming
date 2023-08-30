#!/usr/bin/python3
""" Class creation"""


class Square:
    """Class Object creation"""
    def __init__(self, size=0):
        """creation of object"""
        if size is not int:
            """Check for type"""
            raise TypeError("TypeError")
        if size < 0:
            """check for value"""
            raise ValueError("size must be >= 0")
        self.__size = size
