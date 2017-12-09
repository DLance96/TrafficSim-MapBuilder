import pytest
import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Intersection import Intersection
from src.map.Coordinates import Coordinates
from src.map.Road import Road
from src.map.SpawningProfile import SpawningProfile
from src.map.DriverProfile import DriverProfile
from src.map.VehicleProfile import VehicleProfile


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


def add_connection(intersection, angle, distance, in_ln, out_ln, speed_limit, name):
    """
    Adds an outgoing road to the current intersection.
    :param intersection: intersection where road is added
    :param angle: angle that the road protrudes from the center of the intersection
    :param distance: length of the new road
    :param in_ln: number of incoming lanes for the new road
    :param out_ln: number of outgoing lanes for the new road
    :param: name of road
    :param speed_limit: speed limit of the intersection

    :type intersection: Intersection
    :type angle: float
    :type distance: float
    :type in_ln: int
    :type out_ln: int
    :type name: str
    :type speed_limit: int

    :return: intersection with the new outgoing road connected
    """
    intersection.add_connection(angle, distance, in_ln, out_ln, speed_limit, name)


def add_incoming_connection(intersection, road):
    """
    Adds an incoming road to the current intersection
    :type intersection: Intersection
    :type road: Road
    :return: intersection with new road connected
    """
    intersection.add_incoming_connection(road)


def get_center(center, rad, speed_limit):
    """
    Retrieves the center coordinate of the intersection
    :param center: center coordinate point of the intersection circle
    :param rad: radius of the intersection circle
    :param speed_limit: speed limit of the intersection
    :type center: Coordinates
    :type rad: float
    :type speed_limit: int
    :return: center coordinate point of the intersection circle
    """
    i = Intersection(center, rad, speed_limit)
    return i.get_center()


def get_radius(center, rad, speed_limit):
    """
    Retrieves the radius of the intersection circle
    :param center: center coordinate point of the intersection circle
    :param rad: radius of the intersection circle
    :param speed_limit: speed limit of the intersection
    :type center: Coordinates
    :type rad: float
    :type speed_limit: int
    :return: radius of the intersection circle
    """
    i = Intersection(center, rad, speed_limit)
    return i.get_radius()


def get_speed_limit(center, rad, speed_limit):
    """
    Retrieves the speed limit of the intersection circle
    :param center: center coordinate point of the intersection circle
    :param rad: radius of the intersection circle
    :param speed_limit: speed limit of the intersection
    :type center: Coordinates
    :type rad: float
    :type speed_limit: int
    :return: speed limit of the intersection circle
    """
    i = Intersection(center, rad, speed_limit)
    return i.get_speed_limit()


def get_connections(intersection):
    """
    :param intersection: an intersection object
    :type intersection: Intersection
    :return: the list of objects that the intersection is connected to
    """
    return intersection.get_connections()


def add_spawning_profile(intersection, spawning_profile):
    """
    Adds a spawning profile to an intersection
    :param intersection: intersection
    :param spawning_profile: spawning profile to be added to intersection
    :type intersection: Intersection
    :type spawning_profile: SpawningProfile
    :return: Intersection with spawning profile added to spawning profile list
    """
    return intersection.add_spawning_profile(spawning_profile)


def remove_spawning_profile(intersection, spawning_profile):
    """
    Removes a spawning profile to an intersection
    :param intersection: intersection
    :param spawning_profile: spawning profile to be removed from intersection
    :type intersection: Intersection
    :type spawning_profile: SpawningProfile
    :return: Intersection with spawning profile removed from spawning profile list
    """
    return intersection.remove_spawning_profile(spawning_profile)


def get_spawning_profile_list(intersection):
    """
    Returns the spawning profile list of the intersection
    :param intersection: intersection
    :type intersection: Intersection
    :return: The spawning profile list of the intersection
    """
    return intersection.get_spawning_profile_list()


def add_outgoing_connection(intersection, road):
    """
    Adds an outgoing road to the intersection
    :param intersection: intersection that road will be added to
    :param road: road that will be added to intersection
    :type intersection: Intersection
    :type road: Road
    :return: Updated intersection with updated connections list
    """
    return intersection.add_outgoing_connection(road)


def update_radius(intersection, new_rad):
    """
    Updates the radius of the intersection
    :param intersection: intersection
    :param new_rad: new radius value
    :type intersection: Intersection
    :type new_rad: float
    :return: updated intersection
    """
    return intersection.update_radius(new_rad)


def update_speed_limit(intersection, new_speed):
    """
    Updates the speed limit of the intersection
    :param intersection: intersection
    :param new_speed: new speed value
    :type intersection: Intersection
    :type new_speed: int
    :return: updated intersection
    """
    return intersection.update_speed_limit(new_speed)


def test_update_radius():
    """
    Tests the update_radius function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise
    """
    center = Coordinates(1, 1)
    rad1 = 20.3
    speed = 30

    i = Intersection(center, rad1, speed)

    assert i.get_radius() == 20.3

    i.update_radius(56.5)

    assert i.get_radius() == 56.5


def test_update_speed_limit():
    """
    Tests the update_speed_limit function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise
    """
    center = Coordinates(1, 1)
    rad1 = 20.3
    speed = 30

    i = Intersection(center, rad1, speed)

    assert i.get_speed_limit() == speed

    i.update_speed_limit(27.7)

    assert i.get_speed_limit() == 27.7


def test_add_outgoing_connection():
    """
    Tests the add_outgoing_connection function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise
    """

    center = Coordinates(1 , 1)
    radius = 10
    speed_limit = 20

    i = Intersection(center, radius, speed_limit)
    i2 = Intersection(center, radius, speed_limit)
    i2.add_connection(10.0, 20, 2, 2, 40, 'test2')

    start = Coordinates(1,1)
    end = Coordinates(7, 9)
    len = 15
    out_ln = 2
    in_ln = 1
    ang = 3 * math.pi / 2

    road = Road(start, end, len, out_ln, in_ln, ang, 20, 'Test')

    l = i.get_connections()

    assert not l

    i.add_outgoing_connection(road)

    assert l
    assert l[0].get_length() == 15

    l2 = i2.get_connections()

    assert l2

    i2.add_outgoing_connection(road)

    assert l2
    assert l2[1].get_length() == 15


def test_get_speed_limit():
    """
    Tests the get_speed_limit function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise
    """
    center = Coordinates(1 , 1)
    radius = 10
    speed_limit = 20

    assert get_speed_limit(center, radius, speed_limit) != center
    assert get_speed_limit(center, radius, speed_limit) != radius
    assert get_speed_limit(center, radius, speed_limit) == speed_limit


def test_get_spawning_profile_list():
    """
    Tests the get_spawning_profile_list function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise
    """
    center = Coordinates(1 , 1)
    radius = 10
    speed_limit = 20
    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)
    default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)
    default_spawn = SpawningProfile("Default", default_driver, default_vehicle)

    i = Intersection(center, radius, speed_limit)

    l = i.get_spawning_profile_list()

    assert not l

    i.add_spawning_profile(default_spawn)

    assert l

    assert len(l) == 1

    i.remove_spawning_profile(default_spawn)

    assert len(l) == 0
    assert not l


def test_add_spawning_profile():
    """
    Tests the add_spawning_profile function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise.
    """
    center = Coordinates(1 , 1)
    radius = 10
    speed_limit = 20

    i = Intersection(center, radius, speed_limit)

    assert not i.get_spawning_profile_list()

    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)
    default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)
    default_spawn = SpawningProfile("Default", default_driver, default_vehicle)
    spawn2 = SpawningProfile("spawn2", default_driver, default_vehicle)

    i.add_spawning_profile(default_spawn)

    assert i.get_spawning_profile_list()
    assert len(i.get_spawning_profile_list()) == 1

    i.add_spawning_profile(spawn2)

    assert len(i.get_spawning_profile_list()) == 2


def test_remove_spawning_profile():
    """
    Tests the remove_spawning_profile function
    :return: Test passes if all assertions are ture. Tests do not pass if otherwise.
    """
    center = Coordinates(1 , 1)
    radius = 10
    speed_limit = 20

    i = Intersection(center, radius, speed_limit)

    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)
    default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)
    default_spawn = SpawningProfile("Default", default_driver, default_vehicle)
    spawn2 = SpawningProfile("spawn2", default_driver, default_vehicle)
    spawn_not_in_list = SpawningProfile("spawn3", default_driver, default_vehicle)

    i.add_spawning_profile(default_spawn)
    i.add_spawning_profile(spawn2)

    assert len(i.get_spawning_profile_list()) == 2

    i.remove_spawning_profile(spawn_not_in_list)

    assert len(i.get_spawning_profile_list()) == 2

    i.remove_spawning_profile(spawn2)

    assert len(i.get_spawning_profile_list()) == 1

    i.remove_spawning_profile(default_spawn)

    assert len(i.get_spawning_profile_list()) == 0
    assert not i.get_spawning_profile_list()


def test_is_on_intersection():
    """
    Tests the is_on_connection function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise.
    """
    center = Coordinates(1, 1)
    radius = 10

    i = Intersection(center, radius, 20)

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

    i = Intersection(center, radius, 30)

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

    separate_road = Road(start2, end2, len2, out_ln2, in_ln2, ang2, 20, 'Test')

    ang3 = math.pi / 4
    len3 = 10
    in_ln3 = 5
    out_ln3 = 8

    len4 = 20
    in_ln4 = 25
    out_ln4 = 27
    ang4 = 3 * math.pi / 2

    add_connection(i, ang1, len1, in_ln1, out_ln1, 10, 'Test')

    assert i.get_connections()

    assert len(i.get_connections()) == 1

    assert i.get_connections()[0].get_length() == 20
    assert i.get_connections()[0].get_angle() == ang1
    assert i.get_connections()[0].get_in_lanes() == in_ln1
    assert i.get_connections()[0].get_out_lanes() == out_ln1
    assert i.get_connections()[0].get_angle() == math.pi

    add_connection(i, ang4, len4, in_ln4, out_ln4, 50, 'Test')

    assert i.get_connections()[0].get_length() == 20
    assert i.get_connections()[0].get_angle() == ang1
    assert i.get_connections()[0].get_in_lanes() == in_ln1
    assert i.get_connections()[0].get_out_lanes() == out_ln1
    assert i.get_connections()[0].get_angle() == math.pi
    assert i.get_connections()[1].get_length() == len4
    assert i.get_connections()[1].get_angle() == ang4
    assert i.get_connections()[1].get_in_lanes() == in_ln4
    assert i.get_connections()[1].get_out_lanes() == out_ln4

    add_incoming_connection(i, separate_road)

    assert len(i.get_connections()) == 3

    assert i.get_connections()[0].get_length() == len1
    assert i.get_connections()[0].get_angle() == ang1
    assert i.get_connections()[0].get_in_lanes() == in_ln1
    assert i.get_connections()[0].get_out_lanes() == out_ln1

    assert i.get_connections()[1].get_length() == len4
    assert i.get_connections()[1].get_angle() == ang4
    assert i.get_connections()[1].get_in_lanes() == in_ln4
    assert i.get_connections()[1].get_out_lanes() == out_ln4

    assert i.get_connections()[2].get_length() == len2
    assert i.get_connections()[2].get_angle() == ang2
    assert i.get_connections()[2].get_in_lanes() == in_ln2
    assert i.get_connections()[2].get_out_lanes() == out_ln2

    add_connection(i, ang3, len3, in_ln3, out_ln3, 25, 'Test')

    assert len(i.get_connections()) == 4

    assert i.get_connections()[0].get_length() == len1
    assert i.get_connections()[0].get_angle() == ang1
    assert i.get_connections()[0].get_in_lanes() == in_ln1
    assert i.get_connections()[0].get_out_lanes() == out_ln1

    assert i.get_connections()[1].get_length() == len4
    assert i.get_connections()[1].get_angle() == ang4
    assert i.get_connections()[1].get_in_lanes() == in_ln4
    assert i.get_connections()[1].get_out_lanes() == out_ln4

    assert i.get_connections()[2].get_length() == len2
    assert i.get_connections()[2].get_angle() == ang2
    assert i.get_connections()[2].get_in_lanes() == in_ln2
    assert i.get_connections()[2].get_out_lanes() == out_ln2

    assert i.get_connections()[3].get_length() == len3
    assert i.get_connections()[3].get_angle() == ang3
    assert i.get_connections()[3].get_in_lanes() == in_ln3
    assert i.get_connections()[3].get_out_lanes() == out_ln3


def test_add_incoming_connection():
    """
    Tests the add_incoming_connection function
    :return: Test passes if all assertions are true. Tests do not pass if otherwise.
    """
    center = Coordinates(4, 4)
    radius = 10

    i = Intersection(center, radius, 15)

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

    start3 = Coordinates(7, 8)
    end3 = Coordinates(10, 12)
    len3 = 20
    in_ln3 = 25
    out_ln3 = 27
    ang3 = 3 * math.pi / 2

    r1 = Road(start1, end1, len1, out_ln1, in_ln1, ang1, 20, 'Test')
    r2 = Road(start2, end2, len2, out_ln2, in_ln2, ang2, 25, 'Test')
    r3 = Road(start3, end3, len3, out_ln3, in_ln3, ang3, 30, 'Test')

    add_incoming_connection(i, r1)

    non_empty = i.get_connections()

    assert non_empty

    assert non_empty[0].get_length() == 10
    assert non_empty[0].get_angle() == ang1
    assert non_empty[0].get_in_lanes() == in_ln1
    assert non_empty[0].get_out_lanes() == out_ln1

    add_incoming_connection(i, r3)

    assert len(i.get_connections()) == 2

    assert non_empty[0].get_length() == 10
    assert non_empty[0].get_angle() == ang1
    assert non_empty[0].get_in_lanes() == in_ln1
    assert non_empty[0].get_out_lanes() == out_ln1
    assert non_empty[1].get_length() == len3
    assert non_empty[1].get_angle() == ang3
    assert non_empty[1].get_in_lanes() == in_ln3
    assert non_empty[1].get_out_lanes() == out_ln3

    add_connection(i, math.pi, 20, 21, 22, 40, 'Test')

    assert len(i.get_connections()) == 3
    assert non_empty[0].get_length() == 10
    assert non_empty[0].get_angle() == ang1
    assert non_empty[0].get_in_lanes() == in_ln1
    assert non_empty[0].get_out_lanes() == out_ln1
    assert non_empty[1].get_length() == len3
    assert non_empty[1].get_angle() == ang3
    assert non_empty[1].get_in_lanes() == in_ln3
    assert non_empty[1].get_out_lanes() == out_ln3
    assert non_empty[2].get_length() == 20
    assert non_empty[2].get_angle() == math.pi
    assert non_empty[2].get_in_lanes() == 21
    assert non_empty[2].get_out_lanes() == 22

    add_incoming_connection(i, r2)

    assert len(i.get_connections()) == 4
    assert non_empty[0].get_length() == 10
    assert non_empty[0].get_angle() == ang1
    assert non_empty[0].get_in_lanes() == in_ln1
    assert non_empty[0].get_out_lanes() == out_ln1
    assert non_empty[1].get_length() == len3
    assert non_empty[1].get_angle() == ang3
    assert non_empty[1].get_in_lanes() == in_ln3
    assert non_empty[1].get_out_lanes() == out_ln3
    assert non_empty[2].get_length() == 20
    assert non_empty[2].get_angle() == math.pi
    assert non_empty[2].get_in_lanes() == 21
    assert non_empty[2].get_out_lanes() == 22
    assert non_empty[3].get_length() == 15
    assert non_empty[3].get_angle() == ang2
    assert non_empty[3].get_in_lanes() == in_ln2
    assert non_empty[3].get_out_lanes() == out_ln2


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

    start1 = Coordinates(7, 8)
    end1 = Coordinates(10, 12)
    len1 = 20
    in_ln1 = 25
    out_ln1 = 27
    ang1 = 3 * math.pi / 2

    incoming = Road(start1, end1, len1, out_ln1, in_ln1, ang1, 25, 'Test')

    i1 = Intersection(center, radius, 20)

    empty_connections = get_connections(i1)

    assert not empty_connections

    i2 = Intersection(center, radius, 30)
    add_connection(i2, angle, len, in_ln, out_ln, 40, 'Test')

    non_empty_connections = get_connections(i2)

    assert non_empty_connections
    assert non_empty_connections[0].get_length() == 10
    assert non_empty_connections[0].get_angle() == angle
    assert non_empty_connections[0].get_in_lanes() == in_ln
    assert non_empty_connections[0].get_out_lanes() == out_ln

    add_incoming_connection(i2, incoming)

    assert non_empty_connections[0].get_length() == 10
    assert non_empty_connections[0].get_angle() == angle
    assert non_empty_connections[0].get_in_lanes() == in_ln
    assert non_empty_connections[0].get_out_lanes() == out_ln
    assert non_empty_connections[1].get_length() == len1
    assert non_empty_connections[1].get_angle() == ang1
    assert non_empty_connections[1].get_in_lanes() == in_ln1
    assert non_empty_connections[1].get_out_lanes() == out_ln1

    add_connection(i2, math.pi, 15, 1, 4, 60, 'Test')

    assert non_empty_connections
    assert non_empty_connections[0].get_length() == 10
    assert non_empty_connections[0].get_angle() == angle
    assert non_empty_connections[0].get_in_lanes() == in_ln
    assert non_empty_connections[0].get_out_lanes() == out_ln
    assert non_empty_connections[1].get_length() == len1
    assert non_empty_connections[1].get_angle() == ang1
    assert non_empty_connections[1].get_in_lanes() == in_ln1
    assert non_empty_connections[1].get_out_lanes() == out_ln1
    assert non_empty_connections[2].get_length() == 15
    assert non_empty_connections[2].get_angle() == math.pi
    assert non_empty_connections[2].get_in_lanes() == 1
    assert non_empty_connections[2].get_out_lanes() == 4


def test_get_radius():
    """
    Tests the get_radius function for correctness
    :return: Test passes if all assertions are true. Tests do not pass if otherwise.
    """
    center = Coordinates(7, 3)
    radius = 12

    returned_rad = get_radius(center, radius, 30)

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

    returned_center = get_center(center, radius, 25)

    assert returned_center.get_x() == center.get_x()
    assert returned_center.get_y() == center.get_y()
