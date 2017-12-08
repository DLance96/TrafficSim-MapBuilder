import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from src.map.VehicleProfile import VehicleProfile
from src.map.DriverProfile import DriverProfile
from src.map.SpawningProfile import SpawningProfile


def get_spawning_profile_name(spawn_profile):
    """
    Returns the name of the spawning profile
    :param spawn_profile: the spawning profile
    :type spawn_profile: SpawningProfile
    :return: the name of the spawning profile
    """
    return spawn_profile.get_spawning_profile_name()


def test_get_spawning_profile_name():
    """
    Tests the get_spawning_profile_name function
    :return: Tests pass if spawning profile name is successfully returned. False if otherwise.
    """
    driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)
    vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    test_spawn = SpawningProfile("spawnprofilename!@#", driver, vehicle)

    assert get_spawning_profile_name(test_spawn) != driver
    assert get_spawning_profile_name(test_spawn) != vehicle
    assert get_spawning_profile_name(test_spawn) == "spawnprofilename!@#"


def get_driving_profile(spawn_profile):
    """
    Returns the driving profile of the spawning profile
    :param spawn_profile: the spawning profile
    :type spawn_profile: SpawningProfile
    :return: the driving profile of the spawning profile
    """
    return spawn_profile.get_driver_profile()


def test_get_driving_profile():
    """
    Tests the get_driving_profile function
    :return: Tests pass if spawning profile name is successfully returned. False if otherwise.
    """
    driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)
    vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    test_spawn = SpawningProfile("spawnprofilename!@#", driver, vehicle)

    assert get_driving_profile(test_spawn) == driver
    assert get_driving_profile(test_spawn) != vehicle
    assert get_driving_profile(test_spawn) != "spawnprofilename!@#"


def get_vehicle_profile(spawn_profile):
    """
    Returns the vehicle profile of the spawning profile
    :param spawn_profile: the spawning profile
    :type spawn_profile: SpawningProfile
    :return: the vehicle profile of the spawning profile
    """
    return spawn_profile.get_vehicle_profile()


def test_get_vehicle_profile():
    """
    Tests the get_vehicle_profile function
    :return: Tests pass if spawning profile name is successfully returned. False if otherwise.
    """
    driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)
    vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    test_spawn = SpawningProfile("spawnprofilename!@#", driver, vehicle)

    assert get_vehicle_profile(test_spawn) != driver
    assert get_vehicle_profile(test_spawn) == vehicle
    assert get_vehicle_profile(test_spawn) != "spawnprofilename!@#"


def update_spawning_profile_name(spawn_profile, new_name):
    """
    Updates the name of the spawning profile
    :param new_name: new name of profile
    :param spawn_profile: spawning profile
    :type spawn_profile: SpawningProfile
    :type new_name: str
    :return: updated spawning profile
    """
    return spawn_profile.update_spawning_profile_name(new_name)


def test_update_spawning_profile_name():
    """
    Tests the updates_spawning_profile_name function
    :return: Tests pass if name is updated properly
    """
    driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)
    vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    test_spawn = SpawningProfile("spawnprofilename!@#", driver, vehicle)

    assert test_spawn.get_spawning_profile_name() == "spawnprofilename!@#"

    update_spawning_profile_name(test_spawn, 'updatedname')

    assert test_spawn.get_spawning_profile_name() == "updatedname"


def update_driver_profile(spawn_profile, new_driver):
    """
    Updates the driver profile of the spawning profile
    :param new_driver: new driver profile
    :param spawn_profile: spawning profile
    :type spawn_profile: SpawningProfile
    :type new_driver: DriverProfile
    :return: updated spawning profile
    """
    return spawn_profile.update_driver_profile(new_driver)


def update_vehicle_profile(spawn_profile, new_vehicle):
    """
    Updates the vehicle profile of the spawning profile
    :param new_vehicle: new vehicle profile
    :param spawn_profile: spawning profile
    :type spawn_profile: SpawningProfile
    :type new_vehicle: VehicleProfile
    :return: updated spawning profile
    """
    return spawn_profile.update_vehicle_profile(new_vehicle)


def test_update_vehicle_profile():
    """
    Tests the updates_vehicle_profile function
    :return: Tests pass if name is updated properly
    """
    driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)
    vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    test_spawn = SpawningProfile("spawnprofilename!@#", driver, vehicle)

    assert test_spawn.get_vehicle_profile() == vehicle

    v2 = VehicleProfile("new_vehicle", 5, 10, 1, 1, 500, 70)

    update_vehicle_profile(test_spawn, v2)

    assert test_spawn.get_vehicle_profile() == v2


def test_update_driver_profile():
    """
    Tests the updates_driver_profile function
    :return: Tests pass if name is updated properly
    """
    driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)
    vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    test_spawn = SpawningProfile("spawnprofilename!@#", driver, vehicle)

    assert test_spawn.get_driver_profile() == driver

    driver2 = DriverProfile("test2", 10, 4, 2, 5, 10, 1, 1)

    update_driver_profile(test_spawn, driver2)

    assert test_spawn.get_driver_profile() == driver2
