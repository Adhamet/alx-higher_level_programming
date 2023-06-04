#!/usr/bin/python3
'''
This module has the function add_integer
'''

def add_integer(a, b=98):
    '''returns the addition of a & b'''
    message1 = None
    message2 = None
    if type(a) not in [int, float]:
        message1 = "a"
    if type(b) not in [int, float]:
        message2 = "b"

    for message in [message1, message2]:
        if message != None:
            raise TypeError(message + " must be an integer")

    a, b = int(a), int(b)
    return a + b
