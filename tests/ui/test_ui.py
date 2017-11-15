import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Coordinates import Coordinates
from src.map.Intersection import Intersection
from src.ui.MapBuilder import MapBuilder, AddDialog, TestClass
from PyQt5.QtWidgets import QApplication


def test_map_builder_init():
    """
    Constructs window with Menu Bar for software with intersection of radius 40 centered at (250,250)
    """
    tester = TestClass()
    intersection = tester.map_builder_start()

    assert intersection is not None
    obj = intersection[0]
    assert type(obj) is Intersection
    assert obj.radius == 40
    assert obj.center.x == 250
    assert obj.center.y == 250

def test_add_road():
    """
        Constructs window with Menu Bar for software with intersection of radius 40 centered at (250,250)
        Then adds a road object to existing intersection
    """
