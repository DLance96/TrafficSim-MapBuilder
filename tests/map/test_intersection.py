import pytest
import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Intersection import Intersection
from src.map.Coordinates import Coordinates
from src.map.Road import Road


def is_on_intersection(intersection, coord):
    """
    Determines if coordinates is within intersection
    :param intersection: intersection object
    :param coord: coordinates to test

    :type intersection: Intersection
    :type coord: Coordinates

    :return: True if the coord is within the intersection. False if otherwise.
    """
    return intersection.is_on_intersection(coord)


def add_connection(intersection, angle, distance, in_ln, out_ln):
    """
    Adds an outgoing road to the current intersection.
    :param intersection: intersection where road is added
    :param angle: angle that the road protrudes from the center of the intersection
    :param distance: length of the new road
    :param in_ln: number of incoming lanes for the new road
    :param out_ln: number of outgoing lanes for the new road

    :type intersection: Intersection
    :type angle: float
    :type distance: float
    :type in_ln: int
    :type out_ln: int

    :return: intersection with the new outgoing road connected
    """
    intersection.add_connection(angle, distance, in_ln, out_ln)


def add_incoming_connection(intersection, road):
    """
    Adds an incoming road to the current intersection
    :type intersection: Intersection
    :type road: Road
    :return: intersection with new road connected
    """
    intersection.add_incoming_connection(road)


def get_center(center, rad):
    """
    Retrieves the center coordinate of the intersection
    :param center: center coordinate point of the intersection circle
    :param rad: radius of the intersection circle
    :type center: Coordinates
    :type rad: float
    :return: center coordinate point of the intersection circle
    """
    i = Intersection(center, rad)
    return i.get_center()


def get_radius(center, rad):
    """
    Retrieves the radius of the intersection circle
    :param center: center coordinate point of the intersection circle
    :param rad: radius of the intersection circle
    :type center: Coordinates
    :type rad: float
    :return: radius of the intersection circle
    """
    i = Intersection(center, rad)
    return i.get_radius()


def get_connections(intersection):
    """
    :param intersection: an intersection object
    :type intersection: Intersection
    :return: the list of objects that the intersection is connected to
    """
    return intersection.get_connections()


def test_is_on_connection():
    """
    Tests the is_on_connection function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise.
    """
    center = Coordinates(1, 1)
    radius = 10

    i = Intersection(center, radius)

    in_circle = Coordinates(2, 2)
    not_in_circle = Coordinates(100, 150)
    before_circumference = Coordinates(1, 10.9)
    on_circumference = Coordinates(1, 11)
    after_circumference = Coordinates(1, 11.1)

    assert is_on_intersection(i, in_circle)
    assert is_on_intersection(i, on_circumference)
    assert is_on_intersection(i, before_circumference)
    assert not is_on_intersection(i, not_in_circle)
    assert not is_on_intersection(i, after_circumference)


def test_add_connection():
    """
    Tests the add_connection function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise.
    """
    center = Coordinates(5, 5)
    radius = 3

    i = Intersection(center, radius)

    assert not i.get_connections()

    ang1 = math.pi
    len1 = 20
    in_ln1 = 3
    out_ln1 = 4

    start2 = Coordinates(1,1)
    end2 = Coordinates(7, 9)
    len2 = 15
    out_ln2 = 2
    in_ln2 = 1
    ang2 = 3 * math.pi / 2

    separate_road = Road(start2, end2, len2, out_ln2, in_ln2, ang2)

    ang3 = math.pi / 4
    len3 = 10
    in_ln3 = 5
    out_ln3 = 8

    add_connection(i, ang1, len1, in_ln1, out_ln1)

    assert i.get_connections()

    assert i.get_connections()[0].get_length() == 20
    assert i.get_connections()[0].get_angle() == ang1
    assert i.get_connections()[0].get_in_lanes() == in_ln1
    assert i.get_connections()[0].get_out_lanes() == out_ln1
    assert i.get_connections()[0].get_angle() == math.pi

    add_incoming_connection(i, separate_road)

    add_connection(i, ang3, len3, in_ln3, out_ln3)

    assert i.get_connections()[0].get_length() == len1
    assert i.get_connections()[0].get_angle() == ang1
    assert i.get_connections()[0].get_in_lanes() == in_ln1
    assert i.get_connections()[0].get_out_lanes() == out_ln1

    assert i.get_connections()[2].get_length() == len3
    assert i.get_connections()[2].get_angle() == ang3
    assert i.get_connections()[2].get_in_lanes() == in_ln3
    assert i.get_connections()[2].get_out_lanes() == out_ln3



def test_add_incoming_connection():
    """
    Tests the add_incoming_connection function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise.
    """
    center = Coordinates(4, 4)
    radius = 10

    i = Intersection(center, radius)

    empty_connections = i.get_connections()

    assert not empty_connections

    start1 = Coordinates(1,2)
    end1 = Coordinates(9, 10)
    len1 = 10
    in_ln1 = 3
    out_ln1 = 4
    ang1 = math.pi/2

    start2 = Coordinates(5, 6)
    end2 = Coordinates(12, 14)
    len2 = 15
    in_ln2 = 5
    out_ln2 = 1
    ang2 = math.pi/4

    r1 = Road(start1, end1, len1, out_ln1, in_ln1, ang1)
    r2 = Road(start2, end2, len2, out_ln2, in_ln2, ang2)

    add_incoming_connection(i, r1)

    non_empty = i.get_connections()

    assert non_empty

    assert non_empty[0].get_length() == 10
    assert non_empty[0].get_angle() == ang1
    assert non_empty[0].get_in_lanes() == in_ln1
    assert non_empty[0].get_out_lanes() == out_ln1

    i.add_connection(math.pi, 20, 21, 22)

    add_incoming_connection(i, r2)

    assert len(i.get_connections()) == 3
    assert non_empty[0].get_length() == 10
    assert non_empty[0].get_angle() == ang1
    assert non_empty[0].get_in_lanes() == in_ln1
    assert non_empty[0].get_out_lanes() == out_ln1
    assert non_empty[2].get_length() == 15
    assert non_empty[2].get_angle() == ang2
    assert non_empty[2].get_in_lanes() == in_ln2
    assert non_empty[2].get_out_lanes() == out_ln2


def test_get_connections():
    """
    Tests the get_connections function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise.
    """
    center = Coordinates(1,3)
    radius = 12
    angle = math.pi / 2
    len = 10
    in_ln = 3
    out_ln = 2

    i1 = Intersection(center, radius)

    empty_connections = get_connections(i1)

    assert not empty_connections

    i2 = Intersection(center, radius)
    i2.add_connection(angle, len, in_ln, out_ln)

    non_empty_connections = get_connections(i2)

    assert non_empty_connections
    assert non_empty_connections[0].get_length() == 10
    assert non_empty_connections[0].get_angle() == angle
    assert non_empty_connections[0].get_in_lanes() == in_ln
    assert non_empty_connections[0].get_out_lanes() == out_ln


def test_get_radius():
    """
    Tests the get_radius function for correctness
    :return: Test passes if all assertions are true. Tests do not pass if otherwise.
    """
    center = Coordinates(7, 3)
    radius = 12

    returned_rad = get_radius(center, radius)

    assert returned_rad == radius
    assert returned_rad != center.get_x()
    assert returned_rad != center.get_y()


def test_get_center():
    """
    Tests the get_center function for correctness
    :return: Test passes if all assertions are true. Tests do not pass if otherwise.
    """
    center = Coordinates(7, 3)
    radius = 12

    returned_center = get_center(center, radius)

    assert returned_center.get_x() == center.get_x()
    assert returned_center.get_y() == center.get_y()