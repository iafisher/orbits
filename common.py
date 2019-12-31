import math


def circle_xy(radius, theta):
    """
    For a circle with the given radius centered on the origin, return the (x, y)
    coordinates of the point p on the circle such that the line between p and the origin
    makes an angle of `theta` with the positive x-axis, measured clockwise in radians.
    """
    return (radius * math.cos(theta), radius * math.sin(theta))


def longitude_to_radians(lon):
    if lon >= 0:
        return math.radians(lon)
    else:
        return math.radians(360 + lon)
