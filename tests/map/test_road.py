import pytest
import math
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Coordinates import Coordinates
from src.map.Intersection import Intersection
from src.map.Constants import LANE_WIDTH


def get_points(road):
    """
    Returns the four end points of a road
    :param road: road whose points are extracted and returned
    :type road: Road
    :return: four end points of a road
    """
    return road.get_points()


def is_on_road(road, coord):
    """
    Determines if a coordinate point is within a road
    :param road: road object
    :param coord: coordinates to test

    :type road: Road
    :type coord: Coordinates

    :return: True if the coord is within the road. False if otherwise.
    """
    return road.is_on_road(coord)


def add_start_connection(road, intersection):
    """
    Connects an intersection to the start of the road
    :param road: The road that the intersection will connect to
    :param intersection: The intersection that will connect to the start of the road
    :type road: Road
    :type intersection: Intersection
    :return: None, the road is only updated with a new start connection
    """
    road.add_start_connection(intersection)


def add_end_connection(road, intersection):
    """
    Connects an intersection to the end of the road
    :param road: The road that the intersection will connect to
    :param intersection: The intersection that will connect to the end of the road
    :type road: Road
    :type intersection: Intersection
    :return: None, the road is only updated with a new end connection
    """
    road.add_end_connection(intersection)


def get_start_connection(road):
    """
    Returns the intersection that is connected to the start of the road
    :param road: The road that the intersection is connected to
    :type road: Road

    :return: the intersection that is connected to the start of the road
    """
    return road.get_start_connection()


def get_end_connection(road):
    """
    Returns the intersection that is connected to the end of the road
    :param road: The road that the intersection is connected to
    :type road: Road

    :return: the intersection that is connected to the end of the road
    """
    return road.get_end_connection()


def get_start_coords(start_coords, end_coords, length, out_ln, in_ln, angle):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float

    :return: Start coordinates of a road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle)
    return road.get_start_coords()


def get_end_coords(start_coords, end_coords, length, out_ln, in_ln, angle):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float

    :return: end coordinates of a road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle)
    return road.get_end_coords()


def get_length(start_coords, end_coords, length, out_ln, in_ln, angle):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float

    :return: length of the road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle)
    return road.get_length()


def get_out_lanes(start_coords, end_coords, length, out_ln, in_ln, angle):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float

    :return: number of outgoing lanes for a road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle)
    return road.get_out_lanes()


def get_in_lanes(start_coords, end_coords, length, out_ln, in_ln, angle):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float

    :return: number of incoming lanes for a road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle)
    return road.get_in_lanes()


def get_angle(start_coords, end_coords, length, out_ln, in_ln, angle):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float

    :return: angle that the road protrudes from the center of the intersection.
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle)
    return road.get_angle()


def test_get_points():
    """
    Tests the get_points function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(90, 70)
    end = Coordinates(70, 70)
    length = 20
    out_ln = 1
    in_ln = 1
    angle = math.pi / 2

    road = Road(start, end, length, out_ln, in_ln, angle)

    road_points = road.get_points()

    start_x = start.get_x()
    start_y = start.get_y()
    end_x = end.get_x()
    end_y = end.get_y()

    left = in_ln * LANE_WIDTH
    right = out_ln * LANE_WIDTH

    right_angle = angle + (math.pi / 2.0)
    left_angle = angle - (math.pi / 2.0)

    x_left_of_start = start_x + (left * math.sin(left_angle))
    y_left_of_start = start_y + (left * math.cos(left_angle))

    x_right_of_start = start_x + (right * math.sin(right_angle))
    y_right_of_start = start_y + (right * math.cos(right_angle))

    x_left_of_end = end_x + (left * math.sin(left_angle))
    y_left_of_end = end_y + (left * math.cos(left_angle))

    x_right_of_end = end_x + (right * math.sin(right_angle))
    y_right_of_end = end_y + (right * math.cos(right_angle))

    assert road_points[0].get_x() == x_left_of_start
    assert road_points[0].get_y() == y_left_of_start

    assert road_points[1].get_x() == x_right_of_start
    assert road_points[1].get_y() == y_right_of_start

    assert road_points[2].get_x() == x_right_of_end
    assert road_points[2].get_y() == y_right_of_end

    assert road_points[3].get_x() == x_left_of_end
    assert road_points[3].get_y() == y_left_of_end


def test_is_on_road():
    """
    Tests the is_on_road function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(1, 5)
    end = Coordinates(1, 10)
    len = 10
    out_ln = 3
    in_ln = 2
    angle = math.pi/2

    road = Road(start, end, len, out_ln, in_ln, angle)

    out_of_bounds = Coordinates(14, 25)

    assert not is_on_road(road, out_of_bounds)

    # more testing will need to be conducted after is_on_road is fully implemented.


def test_add_start_connection():
    """
    Tests the add_start_connection function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(3, 3)
    end = Coordinates(2, 1)
    len = 10
    out_ln = 5
    in_ln = 4
    angle = math.pi

    center = Coordinates(1, 2)
    radius = 15

    road = Road(start, end, len, out_ln, in_ln, angle)

    intersection = Intersection(center, radius)

    assert (road.get_start_connection() is None)

    add_start_connection(road, intersection)

    assert (road.get_start_connection() is not None)

    assert road.get_start_connection().get_center().get_x() == center.get_x()
    assert road.get_start_connection().get_center().get_y() == center.get_y()
    assert road.get_start_connection().get_radius() == radius


def test_add_end_connection():
    """
    Tests the add_end_connection function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(3, 3)
    end = Coordinates(2, 1)
    len = 10
    out_ln = 5
    in_ln = 4
    angle = math.pi

    center = Coordinates(1, 2)
    radius = 15

    road = Road(start, end, len, out_ln, in_ln, angle)

    intersection = Intersection(center, radius)

    assert (road.get_end_connection() is None)

    add_end_connection(road, intersection)

    assert (road.get_end_connection() is not None)

    assert road.get_end_connection().get_center().get_x() == center.get_x()
    assert road.get_end_connection().get_center().get_y() == center.get_y()
    assert road.get_end_connection().get_radius() == radius


def test_get_start_connection():
    """
    Tests the get_start_connection function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(2, 2)
    end = Coordinates(3, 4)
    len = 5
    out_ln = 3
    in_ln = 2
    angle = math.pi / 4

    road = Road(start, end, len, out_ln, in_ln, angle)

    center = Coordinates(1, 2)
    radius = 10

    intersection = Intersection(center, radius)

    assert (get_start_connection(road) is None)

    road.start_connection = intersection

    assert (get_start_connection(road) is not None)

    assert get_start_connection(road).get_center().get_x() == 1
    assert get_start_connection(road).get_center().get_y() == 2
    assert get_start_connection(road).get_radius() == 10

    assert (road.get_end_connection() is None)


def test_get_end_connection():
    """
    Tests the get_end_connection function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(2, 2)
    end = Coordinates(3, 4)
    len = 5
    out_ln = 3
    in_ln = 2
    angle = math.pi / 4

    road = Road(start, end, len, out_ln, in_ln, angle)

    center = Coordinates(1, 2)
    radius = 10

    intersection = Intersection(center, radius)

    assert (get_end_connection(road) is None)

    road.end_connection = intersection

    assert (get_end_connection(road) is not None)

    assert get_end_connection(road).get_center().get_x() == 1
    assert get_end_connection(road).get_center().get_y() == 2
    assert get_end_connection(road).get_radius() == 10

    assert (road.get_start_connection() is None)


def test_get_angle():
    """
    Tests the get_angle function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(4, 5)
    end = Coordinates(9, 16)
    length = 7
    out_ln = 3
    in_ln = 2
    angle = (math.pi/2)

    returned_angle = get_angle(start, end, length, out_ln, in_ln, angle)

    assert returned_angle == angle
    assert returned_angle != in_ln
    assert returned_angle != length
    assert returned_angle != out_ln


def test_get_in_lanes():
    """
    Tests the get_in_lanes function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(4, 5)
    end = Coordinates(9, 16)
    length = 7
    out_ln = 3
    in_ln = 2
    angle = (math.pi/2)

    returned_in = get_in_lanes(start, end, length, out_ln, in_ln, angle)

    assert returned_in == in_ln
    assert returned_in != out_ln
    assert returned_in != length


def test_get_out_lanes():
    """
    Tests the get_out_lanes function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(4, 5)
    end = Coordinates(9, 16)
    length = 7
    out_ln = 3
    in_ln = 2
    angle = (math.pi/2)

    returned_out = get_out_lanes(start, end, length, out_ln, in_ln, angle)

    assert returned_out == out_ln
    assert returned_out != in_ln
    assert returned_out != length


def test_get_length():
    """
    Tests the get_length function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(4, 5)
    end = Coordinates(9, 16)
    length = 7
    out_ln = 3
    in_ln = 2
    angle = (math.pi/2)

    returned_len = get_length(start, end, length, out_ln, in_ln, angle)

    assert returned_len == length
    assert returned_len != out_ln
    assert returned_len != in_ln


def test_get_start_coords():
    """
    Tests the get_start_coords function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(4, 5)
    end = Coordinates(9, 16)
    length = 7
    out_ln = 3
    in_ln = 2
    angle = (math.pi/2)

    test_coords = get_start_coords(start, end, length, out_ln, in_ln, angle)

    assert test_coords.get_x() == start.get_x()
    assert test_coords.get_y() == start.get_y()
    assert test_coords.get_x() != end.get_x()
    assert test_coords.get_y() != end.get_y()


def test_get_end_coords():
    """
    Tests the get_end_coords function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(4, 5)
    end = Coordinates(9, 16)
    length = 7
    out_ln = 3
    in_ln = 2
    angle = (math.pi/2)

    test_coords = get_end_coords(start, end, length, out_ln, in_ln, angle)

    assert test_coords.get_x() == end.get_x()
    assert test_coords.get_y() == end.get_y()
    assert test_coords.get_x() != start.get_x()
    assert test_coords.get_y() != start.get_y()
