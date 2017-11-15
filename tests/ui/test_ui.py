import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Coordinates import Coordinates
from src.map.Intersection import Intersection
from src.ui.MapBuilder import MapBuilder, AddDialog, TestClass
from PyQt5.QtWidgets import QApplication


@pytest.mark.first
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


def test_add_dialog_road():
    """
        Add Road to starting intersection using dialog interactions
    """
    tester = TestClass()
    road = tester.add_dialog_road()

    assert road is not None
    obj = road[0]
    assert type(obj) is Road
    assert obj.in_lanes == 1
    assert obj.out_lanes == 1
    assert obj.length == 100
    assert obj.angle == 0


def test_edit_dialog_road():
    """
        Edit Road using dialog interactions
    """
    tester = TestClass()
    obj = tester.edit_dialog_road()

    assert obj is not None
    assert type(obj) is Road
    assert obj.in_lanes == 3
    assert obj.out_lanes == 2
    assert obj.length == 100
    assert obj.angle == 0


def test_add_dialog_intersection():
    """
        Add Intersection to road using dialog interactions
    """
    tester = TestClass()
    intersection = tester.add_dialog_intersection()

    assert intersection is not None
    obj = intersection[1]
    assert type(obj) is Intersection
    assert obj.radius == 40


def test_edit_dialog_intersection():
    """
        Edit Intersection using dialog interactions
    """
    tester = TestClass()
    obj = tester.edit_dialog_intersection()

    assert obj is not None
    assert type(obj) is Intersection
    assert obj.radius == 90
