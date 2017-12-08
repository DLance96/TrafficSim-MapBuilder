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


def get_start_coords(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection
    :param speed_limit: speed limit of road
    :param name: name of road

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float
    :type name: str
    :type speed_limit: int

    :return: Start coordinates of a road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name)
    return road.get_start_coords()


def get_end_coords(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection
    :param speed_limit: speed limit of road
    :param: name of road

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float
    :type name: str
    :type speed_limit: int

    :return: end coordinates of a road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name)
    return road.get_end_coords()


def get_length(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection
    :param: name of road
    :param speed_limit: speed limit of road

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float
    :type name: str
    :type speed_limit: int

    :return: length of the road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name)
    return road.get_length()


def get_out_lanes(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection
    :param: name of road
    :param speed_limit: speed limit of road

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float
    :type name: str
    :type speed_limit: int

    :return: number of outgoing lanes for a road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name)
    return road.get_out_lanes()


def get_in_lanes(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection
    :param: name of road
    :param speed_limit: speed limit of road

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float
    :type name: str
    :type speed_limit: int

    :return: number of incoming lanes for a road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name)
    return road.get_in_lanes()


def get_angle(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection
    :param: name of road
    :param speed_limit: speed limit of road

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float
    :type name: str
    :type speed_limit: int

    :return: angle that the road protrudes from the center of the intersection.
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name)
    return road.get_angle()


def get_name(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection
    :param: name of road
    :param speed_limit: speed limit of road

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float
    :type name: str
    :type speed_limit: int

    :return: name of the road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name)
    return road.get_name()


def get_speed_limit(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name):
    """
    :param start_coords: start coordinates of a road
    :param end_coords: end coordinates of a road
    :param length: length of the road
    :param out_ln: number of outgoing lanes of the road
    :param in_ln: number of incoming lanes of the road
    :param angle: angle of the road protruding from the intersection
    :param: name of road
    :param speed_limit: speed limit of road

    :type start_coords: Coordinates
    :type end_coords: Coordinates
    :type length: float
    :type out_ln: int
    :type in_ln: int
    :type angle: float
    :type name: str
    :type speed_limit: int

    :return: speed limit of the road
    """
    road = Road(start_coords, end_coords, length, out_ln, in_ln, angle, speed_limit, name)
    return road.get_speed_limit()


def update_out_lanes(road, ol):
    """
    Updates the number of out lanes on the road
    :param road: road
    :param ol: new number of out lanes
    :type road: Road
    :type ol: int
    :return: updated road
    """
    road.update_out_lanes(ol)


def test_update_out_lanes():
    """
    Tests the update_out_lanes function
    :return: Tests pass if assertions pass
    """
    start = Coordinates(90, 70)
    end = Coordinates(70, 70)
    length = 20
    out_ln = 2
    in_ln = 1
    angle = math.pi / 2
    speed_limit = 50
    road = Road(start, end, length, out_ln, in_ln, angle, speed_limit, "test")

    assert road.get_out_lanes() == 2

    update_out_lanes(road, 4)

    assert road.get_out_lanes() == 4


def update_in_lanes(road, il):
    """
    Updates the number of in lanes on the road
    :param road: road
    :param il: new number of in lanes
    :type road: Road
    :type il: int
    :return: updated road
    """
    road.update_in_lanes(il)


def test_update_in_lanes():
    """
    Tests the update_in_lanes function
    :return: Tests pass if assertions pass
    """
    start = Coordinates(90, 70)
    end = Coordinates(70, 70)
    length = 20
    out_ln = 2
    in_ln = 1
    angle = math.pi / 2
    speed_limit = 50
    road = Road(start, end, length, out_ln, in_ln, angle, speed_limit, "test")

    assert road.get_in_lanes() == 1

    update_in_lanes(road, 5)

    assert road.get_in_lanes() == 5


def update_speed_limit(road, sl):
    """
    Updates the speed limit of the road
    :param road: road
    :param sl: new speed limit
    :type road: Road
    :type sl: int
    :return: updated road
    """
    road.update_speed_limit(sl)


def test_update_speed_limit():
    """
    Tests the update_speed_limit function
    :return: Tests pass if assertions pass
    """
    start = Coordinates(90, 70)
    end = Coordinates(70, 70)
    length = 20
    out_ln = 2
    in_ln = 1
    angle = math.pi / 2
    speed_limit = 50
    road = Road(start, end, length, out_ln, in_ln, angle, speed_limit, "test")

    assert road.get_speed_limit() == 50

    update_speed_limit(road, 85)

    assert road.get_speed_limit() == 85


def update_name(road, name):
    """
    Updates the name of the road
    :param road: road
    :param name: new name
    :type road: Road
    :type name: str
    :return: updated road
    """
    road.update_name(name)


def test_update_name():
    """
    Tests the update_name function
    :return: Tests pass if assertions pass
    """
    start = Coordinates(90, 70)
    end = Coordinates(70, 70)
    length = 20
    out_ln = 2
    in_ln = 1
    angle = math.pi / 2
    speed_limit = 50
    road = Road(start, end, length, out_ln, in_ln, angle, speed_limit, "test")

    assert road.get_name() == "test"

    update_name(road, "updatedname")

    assert road.get_name() == "updatedname"


def generate_start_connection(road, radius, speed_limit):
    """
    Generates an intersection at the start of a road
    :param road: Road that the intersection will be added to
    :param radius: Radius of the intersection
    :param speed_limit: speed limit of intersection

    :type road: Road
    :type radius: float
    :type speed_limit: int

    :return: A road with an updated start connection
    """
    road.generate_start_connection(radius, speed_limit)


def generate_end_connection(road, radius, speed_limit):
    """
    Generates an intersection at the end of a road
    :param road: Road that the intersection will be connected to
    :param radius: Radius of the intersection
    :param speed_limit: Speed limit of intersection

    :type road: Road
    :type radius: float
    :type speed_limit: int
    :return: A road with an updated end connection
    """
    road.generate_end_connection(radius, speed_limit)


def test_generate_start_connection():
    """
    Tests the generate_start_connection function of Road
    :return: Tests pass if start connection is generated properly. Fail if otherwise.
    """

    start = Coordinates(90, 70)
    end = Coordinates(70, 70)
    length = 20
    out_ln = 1
    in_ln = 1
    angle = math.pi / 2
    speed_limit = 50

    road = Road(start, end, length, out_ln, in_ln, angle, speed_limit, 'Test')

    assert (road.get_start_connection() is None)
    assert (road.get_end_connection() is None)

    generate_start_connection(road, 10, 35)

    assert (road.get_start_connection() is not None)
    assert (road.get_end_connection() is None)

    i = road.get_start_connection()

    assert i.get_radius() == 10
    assert i.get_center().get_x() == 80
    assert i.get_center().get_y() == 70


def test_generate_end_connection():
    """
    Tests the generate_end_connection function of Road
    :return: Tests pass if end connection is generated properly. Fail if otherwise.
    """
    start = Coordinates(90, 70)
    end = Coordinates(70, 70)
    length = 20
    out_ln = 1
    in_ln = 1
    angle = math.pi / 2
    speed_limit = 40

    road = Road(start, end, length, out_ln, in_ln, angle, speed_limit, 'Test')

    assert (road.get_start_connection() is None)
    assert (road.get_end_connection() is None)

    generate_end_connection(road, 15, 25)

    assert (road.get_start_connection() is None)
    assert (road.get_end_connection() is not None)

    i = road.get_end_connection()

    assert i.get_radius() == 15
    assert i.get_center().get_x() == 85
    assert i.get_center().get_y() == 70


def test_get_points():
    """
    Tests the get_points function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(70, 70)
    end = Coordinates(90, 70)
    length = 20
    out_ln = 1
    in_ln = 1
    angle = math.pi / 2
    speed_limit = 40

    road = Road(start, end, length, out_ln, in_ln, angle, speed_limit, 'Test')

    road_points = road.get_points()

    left_start = Coordinates(70, 60)
    right_start = Coordinates(70, 80)
    left_end = Coordinates(90, 60)
    right_end = Coordinates(90, 80)

    assert road_points[0].get_x() == right_start.get_x()
    assert road_points[0].get_y() == right_start.get_y()

    assert road_points[1].get_x() == left_start.get_x()
    assert road_points[1].get_y() == left_start.get_y()

    assert road_points[2].get_x() == left_end.get_x()
    assert road_points[2].get_y() == left_end.get_y()

    assert road_points[3].get_x() == right_end.get_x()
    assert road_points[3].get_y() == right_end.get_y()


def test_is_on_road():
    """
    Tests the is_on_road function
    :return: Asserts true if test cases pass, false if otherwise
    """

    center = Coordinates(1, 1)
    radius = 4
    speed_limit = 25
    i = Intersection(center, radius, speed_limit)

    i.add_connection(math.pi/2, 3, 3, 4, 20, 'Test')

    road = i.get_connections()[0]

    on_border = Coordinates(5.0, -79.0)
    on_border2 = Coordinates(5, 50)
    outside_border = Coordinates(100, 61.01)
    inside_border = Coordinates(7.9, 60.9)
    within_road = Coordinates(6.5, 0)
    outside_road = Coordinates(-70, -70)

    assert road.is_on_road(on_border)
    assert road.is_on_road(within_road)
    assert road.is_on_road(inside_border)
    assert road.is_on_road(on_border2)
    assert not road.is_on_road(outside_border)
    assert not road.is_on_road(outside_road)


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
    speed_limit = 20

    center = Coordinates(1, 2)
    radius = 15

    road = Road(start, end, len, out_ln, in_ln, angle, speed_limit, 'Test')

    intersection = Intersection(center, radius, 25)

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
    speed_limit = 30

    center = Coordinates(1, 2)
    radius = 15

    road = Road(start, end, len, out_ln, in_ln, angle, speed_limit, 'Test')

    intersection = Intersection(center, radius, 15)

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
    speed_limit = 35

    road = Road(start, end, len, out_ln, in_ln, angle, speed_limit, 'Test')

    center = Coordinates(1, 2)
    radius = 10

    intersection = Intersection(center, radius, 20)

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
    speed_limit = 35

    road = Road(start, end, len, out_ln, in_ln, angle, speed_limit, 'Test')

    center = Coordinates(1, 2)
    radius = 10

    intersection = Intersection(center, radius, 25)

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
    speed_limit = 10

    returned_angle = get_angle(start, end, length, out_ln, in_ln, angle, speed_limit, 'Test')

    assert returned_angle == angle
    assert returned_angle != in_ln
    assert returned_angle != length
    assert returned_angle != out_ln


def test_get_name():
    """
    Tests the get_name function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(4, 5)
    end = Coordinates(9, 16)
    length = 7
    out_ln = 3
    in_ln = 2
    angle = (math.pi/2)
    speed_limit = 10

    name = get_name(start, end, length, out_ln, in_ln, angle, speed_limit, 'getnametest')

    assert name != angle
    assert name != in_ln
    assert name != length
    assert name != out_ln
    assert name != speed_limit
    assert name == 'getnametest'


def test_get_speed_limit():
    """
    Tests the get_speed_limit function
    :return: Asserts true if test cases pass, false if otherwise
    """
    start = Coordinates(4, 5)
    end = Coordinates(9, 16)
    length = 7
    out_ln = 3
    in_ln = 2
    angle = (math.pi/2)
    speed_limit = 10

    speed = get_speed_limit(start, end, length, out_ln, in_ln, angle, speed_limit, 'getnametest')

    assert speed != angle
    assert speed != in_ln
    assert speed != length
    assert speed != out_ln
    assert speed == speed_limit
    assert speed != 'getnametest'


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
    speed_limit = 15

    returned_in = get_in_lanes(start, end, length, out_ln, in_ln, angle, speed_limit, 'Test')

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
    speed_limit = 30

    returned_out = get_out_lanes(start, end, length, out_ln, in_ln, angle, speed_limit, 'Test')

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
    speed_limit = 40

    returned_len = get_length(start, end, length, out_ln, in_ln, angle, speed_limit, 'Test')

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
    speed_limit = 20

    test_coords = get_start_coords(start, end, length, out_ln, in_ln, angle, speed_limit, 'Test')

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
    speed_limit = 10

    test_coords = get_end_coords(start, end, length, out_ln, in_ln, angle, speed_limit, 'Test')

    assert test_coords.get_x() == end.get_x()
    assert test_coords.get_y() == end.get_y()
    assert test_coords.get_x() != start.get_x()
    assert test_coords.get_y() != start.get_y()
