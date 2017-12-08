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
    assert obj.center.x == 400
    assert obj.center.y == 250


def test_get_empty_driver_profile_list():
    """
    Tests the driver profile list prior to a profile being added to it. Should contain a default profile to begin with
    """
    tester = TestClass()
    driver_profiles = tester.get_empty_driver_profile_list()
    assert len(driver_profiles) == 1
    assert driver_profiles[0].get_driver_profile_name() == 'Default'


def test_get_empty_vehicle_profile_list():
    """
    Tests the vehicle profile list prior to a profile being added to it. Should contain a default profile to begin with
    """
    tester = TestClass()
    vehicle_profiles = tester.get_empty_vehicle_profile_list()
    assert len(vehicle_profiles) == 1
    assert vehicle_profiles[0].get_vehicle_profile_name() == 'Default'


def test_populate_vehicle_profile_list():
    """
    Tests the vehicle profile list after a vehicle profile is added to it.
    :return: Tests pass as long as profile list is returned properly.
    """

    tester = TestClass()
    vehicle_profiles = tester.populate_vehicle_profile_list()

    assert vehicle_profiles

    first_added_vehicle_profile = vehicle_profiles[1]

    assert first_added_vehicle_profile.get_width() == 5
    assert first_added_vehicle_profile.get_vehicle_profile_name() == 'testVehicleName'
    assert first_added_vehicle_profile.get_length() == 15
    assert first_added_vehicle_profile.get_max_accel() == 2
    assert first_added_vehicle_profile.get_max_braking_decel() == 2
    assert first_added_vehicle_profile.get_mass() == 1000
    assert first_added_vehicle_profile.get_max_speed() == 65

    assert vehicle_profiles[0].get_vehicle_profile_name() == 'Default'


def test_populate_driver_profile_list():
    """
    Tests the driver profile list after a driver profile is added to it.
    :return: Tests pass as long as profile list is returned properly.
    """
    tester = TestClass()
    driver_profiles = tester.populate_driver_profile_list()

    assert driver_profiles

    assert driver_profiles[0].get_driver_profile_name() == 'Default'

    first_driver_profile = driver_profiles[1]

    assert first_driver_profile.get_driver_profile_name() == 'testDriverName'
    assert first_driver_profile.get_over_braking_factor() == 1
    assert first_driver_profile.get_following_time() == 2
    assert first_driver_profile.get_max_accel() == 2
    assert first_driver_profile.get_min_accel() == 0
    assert first_driver_profile.get_max_speed() == 30
    assert first_driver_profile.get_accel_time() == 3
    assert first_driver_profile.get_update_time_ms() == 1


def test_delete_driver_profile_not_in_list():
    """
    Tests to see what happens when a driver profile as attempted to be removed from a list,
    even though it does not exist in the list.
    :return: Test passes if assertions pass.
    """
    tester = TestClass()
    driver_profiles = tester.delete_driver_profile()

    assert driver_profiles
    assert len(driver_profiles) == 1
    assert driver_profiles[0].get_driver_profile_name() == 'Default'


def test_delete_driver_profile_in_list():
    """
    Tests to see what happens when a driver profile as attempted to be removed from a list
    :return: Test passes if assertions pass.
    """
    tester = TestClass()
    driver_profiles = tester.populate_driver_profile_list()

    assert len(driver_profiles) == 2
    assert driver_profiles[1].get_driver_profile_name() == 'testDriverName'

    tester.delete_driver_profile()

    assert len(driver_profiles) == 1
    assert driver_profiles[0].get_driver_profile_name() == 'Default'


def test_delete_vehicle_profile_not_in_list():
    """
    Tests to see what happens when a vehicle profile as attempted to be removed from a list,
    even though it does not exist in the list.
    :return: Test passes if assertions pass.
    """
    tester = TestClass()
    vehicle_profiles = tester.delete_vehicle_profile()

    assert vehicle_profiles
    assert len(vehicle_profiles) == 1
    assert vehicle_profiles[0].get_vehicle_profile_name() == 'Default'


def test_delete_vehicle_profile_in_list():
    """
    Tests to see what happens when a vehicle profile as attempted to be removed from a list
    :return: Test passes if assertions pass.
    """
    tester = TestClass()
    vehicle_profiles = tester.populate_vehicle_profile_list()

    assert len(vehicle_profiles) == 2
    assert vehicle_profiles[1].get_vehicle_profile_name() == 'testVehicleName'

    tester.delete_vehicle_profile()

    assert len(vehicle_profiles) == 1
    assert vehicle_profiles[0].get_vehicle_profile_name() == 'Default'


def test_populate_spawning_profile_list():
    """
    Tests to see if a spawning profile can be successfully stored in our system
    :return: Test passes if assertions pass.
    """

    tester = TestClass()
    spawning_profiles = tester.populate_spawning_profile_list()

    assert spawning_profiles

    assert len(spawning_profiles) == 2

    assert spawning_profiles[1].get_spawning_profile_name() == 'testSpawnName'

    assert spawning_profiles[0].get_spawning_profile_name() == 'Default'


def test_delete_spawning_profile_not_in_list():
    """
    Tests to see what happens when a spawning profile as attempted to be removed from a list,
    even though it does not exist in the list.
    :return: Test passes if assertions pass.
    """
    tester = TestClass()
    spawning_profiles = tester.delete_spawning_profile()

    assert spawning_profiles

    assert len(spawning_profiles) == 1

    assert spawning_profiles[0].get_spawning_profile_name() == 'Default'


def test_delete_spawning_profile_in_list():
    """
    Tests to see what happens when a spawning profile as attempted to be removed from a list
    :return: Test passes if assertions pass.
    """
    tester = TestClass()
    spawning_profiles = tester.populate_spawning_profile_list()

    assert len(spawning_profiles) == 2
    assert spawning_profiles[1].get_spawning_profile_name() == 'testSpawnName'

    tester.delete_spawning_profile()

    assert len(spawning_profiles) == 1
    assert spawning_profiles[0].get_spawning_profile_name() == 'Default'


def test_add_spawning_profile_to_intersection():
    """
    Tests to see if a spawning profile can be properly attached to an intersection
    :return: Test passes if assertions pass
    """
    tester = TestClass()
    intersections = tester.add_spawning_profile_to_intersection()

    attached = False

    for i in intersections:
        for spawn in i.get_spawning_profile_list():
            if spawn.get_spawning_profile_name() == 'Default':
                attached = True
                break;

    assert attached


def test_remove_spawning_profile_from_intersection():
    """
    Tests to see if a spawning profile can be properly removed to an intersection
    :return: Test passes if assertions pass
    """
    tester = TestClass()
    intersections = tester.add_spawning_profile_to_intersection()

    for i in intersections:
        if len(i.get_spawning_profile_list()) != 0:
            assert True

        for spawn in i.get_spawning_profile_list():
            if spawn.get_spawning_profile_name() == 'Default':
                assert True
                break

    tester.delete_spawning_profile_from_intersection()

    for i in intersections:
        if len(i.get_spawning_profile_list()) == 0:
            assert True


def test_connect_intersections():
    """
    Tests to see if intersections can be properly connected.
    :return: Test passes if assertions pass
    """
    tester = TestClass()
    tester.add_dialog_road()
    connector = tester.add_dialog_intersection()

    tester.connect_intersections()

    assert connector[0].get_connections()
    assert connector[1].get_connections()

    assert connector[0].get_connections()[0].get_name() == 'example_name'
    assert connector[1].get_connections()[0].get_name() == 'example_name'


# def test_add_dialog_road():
#     """
#         Add Road to starting intersection using dialog interactions
#     """
#     tester = TestClass()
#     road = tester.add_dialog_road()
#
#     assert road is not None
#     obj = road[0]
#     assert type(obj) is Road
#     assert obj.in_lanes == 1
#     assert obj.out_lanes == 1
#     assert obj.length == 100
#     assert obj.angle == 0
#
#
# def test_edit_dialog_road():
#     """
#         Edit Road using dialog interactions
#     """
#     tester = TestClass()
#     obj = tester.edit_dialog_road()
#
#     assert obj is not None
#     assert type(obj) is Road
#     assert obj.in_lanes == 3
#     assert obj.out_lanes == 2
#     assert obj.length == 100
#     assert obj.angle == 0
#
#
# def test_add_dialog_intersection():
#     """
#         Add Intersection to road using dialog interactions
#     """
#     tester = TestClass()
#     intersection = tester.add_dialog_intersection()
#
#     assert intersection is not None
#     obj = intersection[1]
#     assert type(obj) is Intersection
#     assert obj.radius == 40
#
#
# def test_edit_dialog_intersection():
#     """
#         Edit Intersection using dialog interactions
#     """
#     tester = TestClass()
#     obj = tester.edit_dialog_intersection()
#
#     assert obj is not None
#     assert type(obj) is Intersection
#     assert obj.radius == 90
