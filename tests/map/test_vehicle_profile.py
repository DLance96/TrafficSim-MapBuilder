import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from src.map.VehicleProfile import VehicleProfile


def get_vehicle_profile_name(name, w, l, m_a, m_b_d, mass, m_s):
    """
    Function returns the profile name of the vehicle
    :param name: name of profile
    :param w: width of the vehicle
    :param l: length of the vehicle
    :param m_a: max acceleration of the vehicle
    :param m_b_d: max braking deceleration of the vehicle
    :param mass: mass of the vehicle
    :param m_s: max speed of the vehicle
    :type w: float
    :type l: float
    :type m_a: float
    :type m_b_d: float
    :type mass: float
    :type m_s: float
    :return: profile name of the vehicle
    """

    vehicle = VehicleProfile(name, w, l, m_a, m_b_d, mass, m_s)
    return vehicle.get_vehicle_profile_name()


def test_get_vehicle_profile_name():
    """
    Test function for get_vehicle_profile_name function
    :return: Tests pass if vehicle profile name is returned properly. false if otherwise
    """
    assert get_vehicle_profile_name('test', 10, 20, 2.5, 10.2, 2000, 75) == 'test'
    assert get_vehicle_profile_name('test', 15, 25, 7.2, 13.2, 1520, 90) != 15
    assert get_vehicle_profile_name('test', 15, 25, 7.2, 13.2, 1520, 90) != 25
    assert get_vehicle_profile_name('test', 15, 25, 7.2, 13.2, 1520, 90) != 7.2
    assert get_vehicle_profile_name('test', 15, 25, 7.2, 13.2, 1520, 90) != 13.2
    assert get_vehicle_profile_name('test', 15, 25, 7.2, 13.2, 1520, 90) != 1520
    assert get_vehicle_profile_name('test', 15, 25, 7.2, 13.2, 1520, 90) != 90


def get_width(name, w, l, m_a, m_b_d, mass, m_s):
    """
    Function returns the width of the vehicle
    :param name: name of profile
    :param w: width of the vehicle
    :param l: length of the vehicle
    :param m_a: max acceleration of the vehicle
    :param m_b_d: max braking deceleration of the vehicle
    :param mass: mass of the vehicle
    :param m_s: max speed of the vehicle
    :type w: float
    :type l: float
    :type m_a: float
    :type m_b_d: float
    :type mass: float
    :type m_s: float
    :return: Width of the vehicle
    """

    vehicle = VehicleProfile(name, w, l, m_a, m_b_d, mass, m_s)
    return vehicle.get_width()


def test_get_width():
    """
    Test function for get_width function
    :return: Tests pass if width is returned properly, false if otherwise.
    """

    assert get_width('test', 10, 20, 2.5, 10.2, 2000, 75) == 10
    assert get_width('test', 15, 25, 7.2, 13.2, 1520, 90) != 25
    assert get_width('test', 15, 25, 7.2, 13.2, 1520, 90) != 7.2
    assert get_width('test', 15, 25, 7.2, 13.2, 1520, 90) != 13.2
    assert get_width('test', 15, 25, 7.2, 13.2, 1520, 90) != 1520
    assert get_width('test', 15, 25, 7.2, 13.2, 1520, 90) != 90


def get_length(name, w, l, m_a, m_b_d, mass, m_s):
    """
    Function returns the length of the vehicle
    :param name: name of profile
    :param w: width of the vehicle
    :param l: length of the vehicle
    :param m_a: max acceleration of the vehicle
    :param m_b_d: max braking deceleration of the vehicle
    :param mass: mass of the vehicle
    :param m_s: max speed of the vehicle
    :type w: float
    :type l: float
    :type m_a: float
    :type m_b_d: float
    :type mass: float
    :type m_s: float
    :return: length of the vehicle
    """

    vehicle = VehicleProfile(name, w, l, m_a, m_b_d, mass, m_s)
    return vehicle.get_length()


def test_get_length():
    """
    Test function for get_length function
    :return: Tests pass if length is returned properly, false if otherwise.
    """

    assert get_length('test', 10, 20, 2.5, 10.2, 2000, 75) == 20
    assert get_length('test', 20, 15, 5.2, 12.2, 1235, 88) != 20
    assert get_length('test', 20, 15, 5.2, 12.2, 1235, 88) != 5.2
    assert get_length('test', 20, 15, 5.2, 12.2, 1235, 88) != 12.2
    assert get_length('test', 20, 15, 5.2, 12.2, 1235, 88) != 1235
    assert get_length('test', 20, 15, 5.2, 12.2, 1235, 88) != 88


def get_max_accel(name, w, l, m_a, m_b_d, mass, m_s):
    """
    Function returns the max acceleration of the vehicle
    :param name: name of profile
    :param w: width of the vehicle
    :param l: length of the vehicle
    :param m_a: max acceleration of the vehicle
    :param m_b_d: max braking deceleration of the vehicle
    :param mass: mass of the vehicle
    :param m_s: max speed of the vehicle
    :type w: float
    :type l: float
    :type m_a: float
    :type m_b_d: float
    :type mass: float
    :type m_s: float
    :return: max acceleration of the vehicle
    """

    vehicle = VehicleProfile(name, w, l, m_a, m_b_d, mass, m_s)
    return vehicle.get_max_accel()


def test_get_max_accel():
    """
    Test function for get_max_accel function
    :return: Tests pass if max acceleration is returned properly, false if otherwise.
    """

    assert get_max_accel('test', 10, 20, 2.5, 10.2, 2000, 75) == 2.5
    assert get_max_accel('test', 20, 22, 5.2, 12.5, 2500, 95) != 20
    assert get_max_accel('test', 20, 22, 5.2, 12.5, 2500, 95) != 22
    assert get_max_accel('test', 20, 22, 5.2, 12.5, 2500, 95) != 12.5
    assert get_max_accel('test', 20, 22, 5.2, 12.5, 2500, 95) != 2500
    assert get_max_accel('test', 20, 22, 5.2, 12.5, 2500, 95) != 95


def get_max_braking_decel(name, w, l, m_a, m_b_d, mass, m_s):
    """
    Function returns the max braking deceleration of the vehicle
    :param name: name of profile
    :param w: width of the vehicle
    :param l: length of the vehicle
    :param m_a: max acceleration of the vehicle
    :param m_b_d: max braking deceleration of the vehicle
    :param mass: mass of the vehicle
    :param m_s: max speed of the vehicle
    :type w: float
    :type l: float
    :type m_a: float
    :type m_b_d: float
    :type mass: float
    :type m_s: float
    :return: the max braking deceleration of the vehicle
    """

    vehicle = VehicleProfile(name, w, l, m_a, m_b_d, mass, m_s)
    return vehicle.get_max_braking_decel()


def test_get_max_braking_decel():
    """
    Test function for get_max_braking_decel function
    :return: Tests pass if max braking deceleration is returned properly, false if otherwise.
    """

    assert get_max_braking_decel('test', 10, 20, 2.5, 10.2, 2000, 75) == 10.2
    assert get_max_braking_decel('test', 20, 22, 5.2, 12.5, 2500, 95) != 20
    assert get_max_braking_decel('test', 20, 22, 5.2, 12.5, 2500, 95) != 22
    assert get_max_braking_decel('test', 20, 22, 5.2, 12.5, 2500, 95) != 5.2
    assert get_max_braking_decel('test', 20, 22, 5.2, 12.5, 2500, 95) != 2500
    assert get_max_braking_decel('test', 20, 22, 5.2, 12.5, 2500, 95) != 95


def get_mass(name, w, l, m_a, m_b_d, mass, m_s):
    """
    Function returns the mass of the vehicle
    :param name: name of profile
    :param w: width of the vehicle
    :param l: length of the vehicle
    :param m_a: max acceleration of the vehicle
    :param m_b_d: max braking deceleration of the vehicle
    :param mass: mass of the vehicle
    :param m_s: max speed of the vehicle
    :type w: float
    :type l: float
    :type m_a: float
    :type m_b_d: float
    :type mass: float
    :type m_s: float
    :return: mass of the vehicle
    """

    vehicle = VehicleProfile(name, w, l, m_a, m_b_d, mass, m_s)
    return vehicle.get_mass()


def test_get_mass():
    """
    Test function for get_mass function
    :return: Tests pass if mass is returned properly, false if otherwise.
    """

    assert get_mass('test', 10, 20, 2.5, 10.2, 2000, 75) == 2000
    assert get_mass('test', 20, 22, 5.2, 12.5, 2500, 95) != 20
    assert get_mass('test', 20, 22, 5.2, 12.5, 2500, 95) != 22
    assert get_mass('test', 20, 22, 5.2, 12.5, 2500, 95) != 5.2
    assert get_mass('test', 20, 22, 5.2, 12.5, 2500, 95) != 12.5
    assert get_mass('test', 20, 22, 5.2, 12.5, 2500, 95) != 95


def get_max_speed(name, w, l, m_a, m_b_d, mass, m_s):
    """
    Function returns the max speed of the vehicle
    :param name: name of profile
    :param w: width of the vehicle
    :param l: length of the vehicle
    :param m_a: max acceleration of the vehicle
    :param m_b_d: max braking deceleration of the vehicle
    :param mass: mass of the vehicle
    :param m_s: max speed of the vehicle
    :type w: float
    :type l: float
    :type m_a: float
    :type m_b_d: float
    :type mass: float
    :type m_s: float
    :return: max speed of the vehicle
    """

    vehicle = VehicleProfile(name, w, l, m_a, m_b_d, mass, m_s)
    return vehicle.get_max_speed()


def test_get_max_speed():
    """
    Test function for get_max_speed function
    :return: Tests pass if max speed is returned properly, false if otherwise.
    """

    assert get_max_speed('test', 10, 20, 2.5, 10.2, 2000, 75) == 75
    assert get_max_speed('test', 20, 22, 5.2, 12.5, 2500, 95) != 20
    assert get_max_speed('test', 20, 22, 5.2, 12.5, 2500, 95) != 22
    assert get_max_speed('test', 20, 22, 5.2, 12.5, 2500, 95) != 5.2
    assert get_max_speed('test', 20, 22, 5.2, 12.5, 2500, 95) != 12.5
    assert get_max_speed('test', 20, 22, 5.2, 12.5, 2500, 95) != 2500


def update_width(vehicle, width):
    """
    Updates the width of the vehicle
    :param vehicle: vehicle
    :param width: new vehicle width
    :type vehicle: VehicleProfile
    :type width: int
    :return: Updated vehicle
    """
    return vehicle.update_width(width)


def update_length(vehicle, length):
    """
    Updates the length of the vehicle
    :param vehicle: vehicle
    :param length: new vehicle length
    :type vehicle: VehicleProfile
    :type length: int
    :return: Updated vehicle
    """
    return vehicle.update_length(length)


def update_max_accel(vehicle, ma):
    """
    Updates the max accel of the vehicle
    :param vehicle: vehicle
    :param ma: new max accel
    :type vehicle: VehicleProfile
    :return: Updated vehicle
    """
    return vehicle.update_max_accel(ma)


def update_max_braking_decel(vehicle, mbd):
    """
    Updates the max braking decel of the vehicle
    :param vehicle: vehicle
    :param mbd: new max braking decel
    :type vehicle: VehicleProfile
    :return: Updated vehicle
    """
    return vehicle.update_max_braking_decel(mbd)


def update_mass(vehicle, mass):
    """
    Updates the mass of the vehicle
    :param vehicle: vehicle
    :param mass: new mass
    :type vehicle: VehicleProfile
    :return: Updated vehicle
    """
    return vehicle.update_mass(mass)


def update_max_speed(vehicle, speed):
    """
    Updates the max speed of the vehicle
    :param vehicle: vehicle
    :param speed: new max speed
    :type vehicle: VehicleProfile
    :return: Updated vehicle
    """
    return vehicle.update_max_speed(speed)


def update_profile_name(vehicle, name):
    """
    Updates the name of the vehicle
    :param vehicle: vehicle
    :param name: new name
    :type vehicle: VehicleProfile
    :return: Updated vehicle
    """
    return vehicle.update_profile_name(name)


def test_update_width():
    """
    Tests the update_width function
    :return: Passes if width is properly updated
    """
    default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    assert default_vehicle.get_width() == 5

    update_width(default_vehicle, 10)

    assert default_vehicle.get_width() == 10


def test_update_name():
    """
    Tests the update_name function
    :return: Passes if name is properly updated
    """
    default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    assert default_vehicle.get_vehicle_profile_name() == "Default"

    update_profile_name(default_vehicle, "updatenametest")

    assert default_vehicle.get_vehicle_profile_name() == "updatenametest"


def test_update_max_accel():
    """
    Tests the update_max_accel function
    :return: Passes if max accel is properly updated
    """
    default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    assert default_vehicle.get_max_accel() == 2

    update_max_accel(default_vehicle, 22)

    assert default_vehicle.get_max_accel() == 22


def test_update_length():
    """
    Tests the update_length function
    :return: Passes if length is properly updated
    """
    default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    assert default_vehicle.get_length() == 15

    update_length(default_vehicle, 25)

    assert default_vehicle.get_length() == 25


def test_update_max_braking_decel():
    """
    Tests the update_max_braking_decel function
    :return: Passes if braking decel is properly updated
    """
    default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    assert default_vehicle.get_max_braking_decel() == 2

    update_max_braking_decel(default_vehicle, 40)

    assert default_vehicle.get_max_braking_decel() == 40


def test_update_mass():
    """
    Tests the update_mass function
    :return: Passes if mass is properly updated
    """
    default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    assert default_vehicle.get_mass() == 1000

    update_mass(default_vehicle, 500)

    assert default_vehicle.get_mass() == 500


def test_update_max_speed():
    """
    Tests the update_max_speed function
    :return: Passes if max speed is properly updated
    """
    default_vehicle = VehicleProfile("Default", 5, 15, 2, 2, 1000, 65)

    assert default_vehicle.get_max_speed() == 65

    update_max_speed(default_vehicle, 80)

    assert default_vehicle.get_max_speed() == 80
