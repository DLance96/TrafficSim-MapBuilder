import pytest
import sys
import os
import math
import filecmp

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.xml_parse.Import import *
from src.map.Intersection import Intersection


def test_in_intersection():
    intersection = Intersection(Coordinates(0, 0), 10)

    assert in_intersection(intersection, Coordinates(1, 1))
    assert in_intersection(intersection, Coordinates(0, 9.9))
    assert not in_intersection(intersection, Coordinates(11, 1))
    assert not in_intersection(intersection, Coordinates(10.1, 0))


def test_get_chord_center():

    chord_center = get_chord_center(0, 10, Coordinates(0, -5))
    x = chord_center.get_x()
    y = chord_center.get_y()
    checkx = -.1 < x < .1
    checky = -.1 < y < .1
    assert checkx
    print(y)
    assert y == 0


def test_generate_road():
    with pytest.raises(XMLFormatError):
        import_xml("{}/resources/road1.xml".format(os.path.dirname(__file__)))
    with pytest.raises(XMLFormatError):
        import_xml("{}/resources/road2.xml".format(os.path.dirname(__file__)))
    with pytest.raises(XMLFormatError):
        import_xml("{}/resources/road3.xml".format(os.path.dirname(__file__)))
    with pytest.raises(XMLFormatError):
        import_xml("{}/resources/road4.xml".format(os.path.dirname(__file__)))
    with pytest.raises(XMLFormatError):
        import_xml("{}/resources/road5.xml".format(os.path.dirname(__file__)))
    with pytest.raises(XMLFormatError):
        import_xml("{}/resources/road6.xml".format(os.path.dirname(__file__)))
    with pytest.raises(XMLFormatError):
        import_xml("{}/resources/road7.xml".format(os.path.dirname(__file__)))