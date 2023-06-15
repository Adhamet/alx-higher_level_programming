#!/usr/bin/python3
"""Module that contains Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class inherited from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string info about this square."""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
