import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from src.map.Coordinates import Coordinates


def get_coord_x(x, y):
    """
    Function returns the x value of the coordinate
    :param x: x value of coordinate
    :param y: y value of coordinate

    :return: x value of coordinate
    """
    coord = Coordinates(x, y)
    return coord.get_x()


def test_coord_x():
    """
    Test function for coord_x function
    :return: Tests pass if x coordinate is returned in all cases, false if otherwise.
    """
    assert get_coord_x(3, 2) == 3
    assert get_coord_x(3, 2) != 2
    assert get_coord_x(2.4, 26.2) == 2.4
    assert get_coord_x(2.4, 26.2) != 26.2
    assert get_coord_x(.2234, .7337) == .2234
    assert get_coord_x(.2234, .7337) != .7337


def get_coord_y(x, y):
    """
    Function returns the y value of the coordinate
    :param x: x value of coordinate
    :param y: y value of coordinate

    :return: y value of coordinate
    """
    coord = Coordinates(x, y)
    return coord.get_y()


def test_coord_y():
    """
    Test function for coord_y function
    :return: Tests pass if y coordinate is returned in all cases, false if otherwise.
    """
    assert get_coord_y(3, 2) == 2
    assert get_coord_y(3, 2) != 3
    assert get_coord_y(2.4, 26.2) == 26.2
    assert get_coord_y(2.4, 26.2) != 2.4
    assert get_coord_y(.2234, .7337) == .7337
    assert get_coord_y(.2234, .7337) != .2234



