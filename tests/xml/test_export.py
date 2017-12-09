import pytest
import sys
import os
from math import isclose

from src.map.DriverProfile import DriverProfile
from src.map.SpawningProfile import SpawningProfile
from src.map.VehicleProfile import VehicleProfile
from src.map.Road import Road
from src.map.Intersection import Intersection
import src.xml_parse.Exceptions as EX
import filecmp
from src.xml_parse.Export import *
from src.xml_parse.Utils import *


def test_convert_road_to_simulation_size():
    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi, 60, "road")
    length, anchor_point = convert_road_to_simulation_size(road)

    assert math.isclose(length, 20, rel_tol=.1)
    assert math.isclose(anchor_point.x, 80, rel_tol=.1)
    assert math.isclose(anchor_point.y, 70, rel_tol=.1)

    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi, 60, "road")
    intersection = Intersection(Coordinates(110, 70), 20, 30)
    intersection.add_outgoing_connection(road)
    road.add_start_connection(intersection)

    length, anchor_point = convert_road_to_simulation_size(road)

    assert math.isclose(length, 22.67949192431123, rel_tol=.1)
    assert math.isclose(anchor_point.x, 100, rel_tol=.1)
    assert math.isclose(anchor_point.y, 52.679491924311236, rel_tol=.1)

    intersection = Intersection(Coordinates(50, 70), 20, 30)
    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi, 60, "road")
    intersection.add_incoming_connection(road)
    road.add_end_connection(intersection)
    length, anchor_point = convert_road_to_simulation_size(road)

    assert math.isclose(length, 22.67949192431123, rel_tol=.1)
    assert math.isclose(anchor_point.x, 80, rel_tol=.1)
    assert math.isclose(anchor_point.y, 70, rel_tol=.1)


def test_make_xml():
    roads = []
    intersections = []
    intersection = Intersection(Coordinates(50, 70), 20, 40)
    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi, 60, "road")
    driver = DriverProfile("a", .1, 3, 6, 0, 200, 10, 30)
    vehicle = VehicleProfile("a", 5, 5, 5, .1, 200, 200)
    spawning = SpawningProfile("a", driver, vehicle)
    intersection.add_incoming_connection(road)
    intersection.add_spawning_profile(spawning)
    intersection.add_cycle("cycle", [0], 2000)
    road.add_end_connection(intersection)
    roads.append(road)
    intersections.append(intersection)
    export_xml(roads, intersections, "{}/temp.xml".format(os.path.dirname(__file__)))

    assert filecmp.cmp("{}/temp.xml".format(os.path.dirname(__file__)),
                       "{}/resources/make_xml.xml".format(os.path.dirname(__file__)))

    os.remove("{}/temp.xml".format(os.path.dirname(__file__)))
    assert not os.path.isfile("{}/temp.xml".format(os.path.dirname(__file__)))

    roads = []
    intersections = []
    intersection = Intersection(Coordinates(50, 70), 20, 40)
    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi, 60, "road")
    roads.append(road)
    intersections.append(intersection)
    with pytest.raises(EX.XMLFormatError) as context:
        export_xml(roads, intersections, "{}/temp.xml".format(os.path.dirname(__file__)))
    assert context.match('Map is not connected')

    assert not os.path.isfile("{}/temp.xml".format(os.path.dirname(__file__)))


def test_export_xml():
    roads = []
    intersections = []
    intersection = Intersection(Coordinates(50, 70), 20, 40)
    road = Road(Coordinates(90, 70), Coordinates(70, 70), 20, 1, 1, math.pi, 60, "road")
    roads.append(road)
    intersections.append(intersection)
    # os.remove("{}/temp.xml".format(os.path.dirname(__file__)))
    assert not os.path.isfile("{}/temp.xml".format(os.path.dirname(__file__)))
    with pytest.raises(EX.XMLFormatError) as context:
        export_xml(roads, intersections, "{}/temp.xml".format(os.path.dirname(__file__)))
    assert not os.path.isfile("{}/temp.xml".format(os.path.dirname(__file__)))


def test_utils():
    assert add_angles(0, 4 * math.pi) == 0
    assert add_angles(math.pi, math.pi / 2) == 3* math.pi / 2

    assert distance(Coordinates(0, 0), Coordinates(0, 1)) == 1

    roads = ['a', 'b', 'c']
    visited = ['c', 'b']
    temp = remove_visited_roads(roads, visited)
    assert len(temp) == 1

    check_overload_intersection([])
