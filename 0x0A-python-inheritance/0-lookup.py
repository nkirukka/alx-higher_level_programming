#!/usr/bin/python3
 """this module returns the list of available attributes and methods of an object"""


def lookup(obj):
    """returns the list of available attributes and methods of an object
    Args:
        obj (object): object
    """
    return dir(obj)
