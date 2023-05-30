#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except BaseException as err:
        result = None
        print("Exceptipn = {}".format(err), file=sys.stderr)
    finally:
        return result
