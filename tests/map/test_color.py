import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from src.map.Color import Color


def get_r(r, g, b):
    """
    Function returns the red value of the RGB color
    :param r: red component of the RGB color
    :param g: green component of the RGB color
    :param b: blue component of the RGB color
    :return: red component of the RGB color
    """

    color = Color(r, g, b)
    return color.get_r()


def test_get_r():
    """
    Test function for get_r function
    :return: Tests pass if r component is returned properly, false if otherwise.
    """

    assert get_r(100, 143, 255) == 100
    assert get_r(100, 143, 255) != 143
    assert get_r(100, 143, 255) != 255


def get_g(r, g, b):
    """
    Function returns the green value of the RGB color
    :param r: red component of the RGB color
    :param g: green component of the RGB color
    :param b: blue component of the RGB color
    :return: green component of the RGB color
    """

    color = Color(r, g, b)
    return color.get_g()


def test_get_g():
    """
    Test function for get_g function
    :return: Tests pass if g component is returned properly, false if otherwise.
    """

    assert get_g(100, 143, 255) != 100
    assert get_g(100, 143, 255) == 143
    assert get_g(100, 143, 255) != 255


def get_b(r, g, b):
    """
    Function returns the blue value of the RGB color
    :param r: red component of the RGB color
    :param g: green component of the RGB color
    :param b: blue component of the RGB color
    :return: blue component of the RGB color
    """

    color = Color(r, g, b)
    return color.get_b()


def test_get_b():
    """
    Test function for get_b function
    :return: Tests pass if b component is returned properly, false if otherwise.
    """

    assert get_b(100, 143, 255) != 100
    assert get_b(100, 143, 255) != 143
    assert get_b(100, 143, 255) == 255


def update_r(color, new_r):
    """
    Function updates the red component of the RGB color
    :param color: RGB color to be modified
    :param new_r: new r component value

    :type color: Color
    :type new_r: int

    :return: Updated RGB color with new r component
    """

    color.update_r(new_r)


def test_update_r():
    """
    Test function for update_r function
    :return: Tests pass if r component is updated properly, false if otherwise.
    """

    color = Color(100, 142, 438)

    assert color.get_r() == 100
    assert color.get_g() == 142
    assert color.get_b() == 438

    update_r(color, 202)

    assert color.get_r() == 202
    assert color.get_g() == 142
    assert color.get_b() == 438


def update_g(color, new_g):
    """
    Function updates the green component of the RGB color
    :param color: RGB color to be modified
    :param new_g: new g component value

    :type color: Color
    :type new_g: int

    :return: Updated RGB color with new g component
    """

    color.update_g(new_g)


def test_update_g():
    """
    Test function for update_g function
    :return: Tests pass if g component is updated properly, false if otherwise.
    """
    color = Color(100, 142, 438)

    assert color.get_r() == 100
    assert color.get_g() == 142
    assert color.get_b() == 438

    update_g(color, 239)

    assert color.get_r() == 100
    assert color.get_g() == 239
    assert color.get_b() == 438


def update_b(color, new_b):
    """
    Function updates the blue component of the RGB color
    :param color: RGB color to be modified
    :param new_b: new b component value

    :type color: Color
    :type new_b: int

    :return: Updated RGB color with new b component
    """

    color.update_b(new_b)


def test_update_b():
    """
    Test function for update_b function
    :return: Tests pass if b component is updated properly, false if otherwise.
    """
    color = Color(100, 142, 438)

    assert color.get_r() == 100
    assert color.get_g() == 142
    assert color.get_b() == 438

    update_b(color, 47)

    assert color.get_r() == 100
    assert color.get_g() == 143
    assert color.get_b() == 47
