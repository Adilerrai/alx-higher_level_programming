#!/usr/bin/python3
""" Class creation"""


class Square:
    """Class Object creation"""
    def __init__(self, size=0):
        '''creation of object

        Args:
            size (int): The size of the Square object
        '''
        if not isinstance(size, int):
            raise TypeError("TypeError")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size