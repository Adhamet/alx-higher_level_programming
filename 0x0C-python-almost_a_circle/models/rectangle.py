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
        self.__width = value

    @property
    def height(self):
        """Height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        self.__height = value

    @property
    def x(self):
        """X of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x of rectangle"""
        self.__x = value

    @property
    def y(self):
        """Set y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y of rectangle"""
        self.__y = value
