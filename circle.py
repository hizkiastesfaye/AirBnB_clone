from math import pi


def Circle(r):
    if r < 0:
        raise ValueError("The radius should be greater than Zero")
    if type(r) not in [int, float]:
        raise TypeError("the radius is not int or float")
    return pi*(r**2)
