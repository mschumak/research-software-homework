# Michael Schumaker
# Building Research Software Day 3 Homework

from math import pi

def calc_area_square(side_length: float) -> float:
    """Return the area of a square with a given side length."""
    if side_length < 0:
        raise ValueError(
            f'side_length must not be negative, got {side_length}')
    return side_length**2

def calc_area_circle(radius: float) -> float:
    """Return the area of a circle with a given radius."""
    if radius < 0:
        raise ValueError(
            f'radius must not be negative, got {radius}')
    return pi * radius**2

