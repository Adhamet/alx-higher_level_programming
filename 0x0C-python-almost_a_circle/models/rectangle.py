#!/usr/bin/python3
"""
This module contains the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    A rectangle class inherited from Base class

    Attributes:
        width: width of rectangle
        height: height of rectangle
        x
        y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """X of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x of rectangle"""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Set y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y of rectangle"""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, sw=True):
        """Method to validate the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if sw and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not sw and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''Computes area of rectangle.'''
        return self.width * self.height

    def display(self):
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.__width + '\n') * self.__height
        print(s, end='')

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)
