#!/usr/bin/python3

def add_integer(a, b=98):
    message1 = None
    message2 = None
    if type(a) not in [int, float]:
        message1 = "a"
    if type(b) not in [int, float]:
        message2 = "b"

    for message in [message1, message2]:
        if message != None:
            raise TypeError(message + " must be an integer")

    a = int(a)
    b = int(b)
    return int(a + b)
