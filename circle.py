#!/usr/bin/python3
from math import pi
""" python code that passes the pycodestyle"""


def Circle(r):
    """ circle function that result the area of circle """

    if r < 0:
        raise ValueError("The radius should be greater than Zero")
    if type(r) not in [int, float]:
        raise TypeError("the radius is not int or float")
    return pi*(r**2)
