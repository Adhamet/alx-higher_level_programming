#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    check = True
    try:
        print("{:d}".format(value))
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
        check = False
    return check
