#!/usr/bin/python3
'''
This module includes the say_my_name function
'''


def say_my_name(first_name, last_name = ""):
    '''Prints out full name of a person'''
    msg1 = None
    msg2 = None
    if type(first_name) is not str:
        msg1 = "first_name"
    if type(last_name) is not str:
        msg2 = "last_name"

    for msg in [msg1, msg2]:
        if msg is not None:
            raise TypeError(msg + " must be a string")
    print("My name is {} {}".format(first_name, last_name))
