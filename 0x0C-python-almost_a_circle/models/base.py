#!/usr/bin/python3
"""
This module contains Base class
"""


class Base:
    """
    A basic class for up-coming classes

    Attributes: __nb_objects, the current number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
