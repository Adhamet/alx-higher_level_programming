#!/usr/bin/python3
"""
Contains inherits_from func
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass otherwise false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
