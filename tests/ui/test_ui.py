import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Coordinates import Coordinates
from src.map.Intersection import Intersection
from src.ui.MapBuilder import MapBuilder, AddDialog, TestClass
from PyQt5.QtWidgets import QApplication


# @pytest.mark.first
# def test_map_builder_init():
#     """
#     Constructs window with Menu Bar for software with intersection of radius 40 centered at (250,250)
#     """
#     tester = TestClass()
#     intersection = tester.map_builder_start()
#
#     assert intersection is not None
#     obj = intersection[0]
#     assert type(obj) is Intersection
#     assert obj.radius == 40
#     assert obj.center.x == 250
#     assert obj.center.y == 250
#
#
# def test_get_empty_driver_profile_list():
#     """
#     Tests the driver profile list prior to a profile being added to it.
#     """
#     tester = TestClass()
#     driver_profiles = tester.get_empty_driver_profile_list()
#     assert not driver_profiles
#
#
# def test_get_empty_vehicle_profile_list():
#     """
#     Tests the vehicle profile list prior to a profile being added to it.
#     """
#     tester = TestClass()
#     vehicle_profiles = tester.get_empty_vehicle_profile_list()
#     assert not vehicle_profiles
#
#
# def test_populate_vehicle_profile_list():
#     """
#     Tests the vehicle profile list after a vehicle profile is added to it.
#     :return: Tests pass as long as profile list is returned properly.
#     """
#     tester = TestClass()
#     vehicle_profiles = tester.populate_vehicle_profile_list()
#
#     first_vehicle_profile = vehicle_profiles[0]
#
#     assert vehicle_profiles
#
#     assert first_vehicle_profile.get_width() == 5
#     assert first_vehicle_profile.get_vehicle_profile_name() == 'testVehicleName'
#     assert first_vehicle_profile.get_length() == 15
#     assert first_vehicle_profile.get_max_accel() == 2
#     assert first_vehicle_profile.get_max_braking_decel() == 2
#     assert first_vehicle_profile.get_mass() == 1000
#     assert first_vehicle_profile.get_max_speed() == 65
#
#
# def test_populate_driver_profile_list():
#     """
#     Tests the driver profile list after a driver profile is added to it.
#     :return: Tests pass as long as profile list is returned properly.
#     """
#     tester = TestClass()
#     driver_profiles = tester.populate_driver_profile_list()
#
#     first_driver_profile = driver_profiles[0]
#
#     assert driver_profiles
#
#     assert first_driver_profile.get_driver_profile_name() == 'testDriverName'
#     assert first_driver_profile.get_over_braking_factor() == 1
#     assert first_driver_profile.get_following_time() == 2
#     assert first_driver_profile.get_max_accel() == 2
#     assert first_driver_profile.get_min_accel() == 0
#     assert first_driver_profile.get_max_speed() == 30
#     assert first_driver_profile.get_accel_time() == 3
#     assert first_driver_profile.get_update_time_ms() == 1
#
#
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
