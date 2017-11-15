import pytest
import sys
import os
import math
import filecmp

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.xml_parse.Export import *


def test_convert_road_to_simulation_size():
    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi)
    length, anchor_point = convert_road_to_simulation_size(road)

    assert length == 20
    assert anchor_point.x == 90
    assert anchor_point.y == 90

    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi)
    intersection = Intersection(Coordinates(110, 70), 20)
    intersection.add_outgoing_connection(road)
    road.add_start_connection(intersection)

    length, anchor_point = convert_road_to_simulation_size(road)

    assert length == 40
    assert anchor_point.x == 110
    assert anchor_point.y == 90

    intersection = Intersection(Coordinates(50, 70), 20)
    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi)
    intersection.add_incoming_connection(road)
    road.add_end_connection(intersection)
    length, anchor_point = convert_road_to_simulation_size(road)

    assert length == 40
    assert anchor_point.x == 90
    assert anchor_point.y == 90


def test_make_xml():
    roads = []
    intersections = []
    intersection = Intersection(Coordinates(50, 70), 20)
    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi)
    intersection.add_incoming_connection(road)
    road.add_end_connection(intersection)
    roads.append(road)
    intersections.append(intersection)
    export_xml(roads, intersections, "{}/temp.xml".format(os.path.dirname(__file__)))

    assert filecmp.cmp("{}/temp.xml".format(os.path.dirname(__file__)),
                       "{}/resources/make_xml.xml".format(os.path.dirname(__file__)))

    os.remove("{}/temp.xml".format(os.path.dirname(__file__)))


def test_export_xml():
    roads = []
    intersections = []
    intersection = Intersection(Coordinates(50, 70), 20)
    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi)
    roads.append(road)
    intersections.append(intersection)
    assert not os.path.isfile("{}/temp.xml".format(os.path.dirname(__file__)))
    export_xml(roads, intersections, "{}/temp.xml".format(os.path.dirname(__file__)))
    assert not os.path.isfile("{}/temp.xml".format(os.path.dirname(__file__)))
