#!/usr/bin/python3
"""Defines an empty class rectangle"""


class Rectangle:
    """Class that defines properties of rectangle:

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initializes new instances of the rectangle

        Args:
            width (int, optional): width of rectangle, defaults to 0
            height (int, optional): height of rectangle, defaults to 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width getter

        Returns:
            int: width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """Height getter

        Returns:
            int: height of rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property (WIDTH) setter

        Args:
            value (int): width of rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property (HEIGHT) setter

        Args:
            value (int): height of rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
