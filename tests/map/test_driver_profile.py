import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from src.map.DriverProfile import DriverProfile


def get_driver_profile_name(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the profile name of the driver
    :param name: name of profile
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type name: str
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the driver profile name of the driver
    """

    driver = DriverProfile(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_driver_profile_name()


def test_get_driver_profile_name():
    """
    Test function for get_driver_profile_name function
    :return: Tests pass if driver profile name is returned properly, false if otherwise.
    """

    assert get_driver_profile_name('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 'test'
    assert get_driver_profile_name('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 1.2
    assert get_driver_profile_name('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.4
    assert get_driver_profile_name('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 25.2
    assert get_driver_profile_name('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 2.2
    assert get_driver_profile_name('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 75.0
    assert get_driver_profile_name('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_driver_profile_name('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_over_braking_factor(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the over braking factor of the driver
    :param name: name of profile
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type name: str
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the overbraking factor of the driver
    """

    driver = DriverProfile(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_over_braking_factor()


def test_get_over_braking_factor():
    """
    Test function for get_over_braking_factor function
    :return: Tests pass if over braking factor is returned properly, false if otherwise.
    """

    assert get_over_braking_factor('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 1.2
    assert get_over_braking_factor('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.4
    assert get_over_braking_factor('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 25.2
    assert get_over_braking_factor('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 2.2
    assert get_over_braking_factor('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 75.0
    assert get_over_braking_factor('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_over_braking_factor('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_following_time(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the following time of the driver
    :param name: name of profile
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type name: str
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the following time of the driver
    """
    driver = DriverProfile(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_following_time()


def test_get_following_time():
    """
    Test function for get_following_time function
    :return: Tests pass if following time is returned properly, false if otherwise.
    """

    assert get_following_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 3.4
    assert get_following_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 1.2
    assert get_following_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 25.2
    assert get_following_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 2.2
    assert get_following_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 75.0
    assert get_following_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_following_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_max_accel(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the max acceleration of the driver
    :param name: name of profile
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type name: str
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the max acceleration that the driver is comfortable with
    """
    driver = DriverProfile(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_max_accel()


def test_get_max_accel():
    """
    Test function for get_max_accel function
    :return: Tests pass if maximum acceleration is returned properly, false if otherwise.
    """

    assert get_max_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 25.2
    assert get_max_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 1.2
    assert get_max_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.4
    assert get_max_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 2.2
    assert get_max_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 75.0
    assert get_max_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_max_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_min_accel(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the min acceleration of the driver
    :param name: name of profile
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type name: str
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the min acceleration that the driver is comfortable with
    """
    driver = DriverProfile(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_min_accel()


def test_get_min_accel():
    """
    Test function for get_min_accel function
    :return: Tests pass if minimum acceleration is returned properly, false if otherwise.
    """

    assert get_min_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 2.2
    assert get_min_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 1.2
    assert get_min_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.4
    assert get_min_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 25.2
    assert get_min_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 75.0
    assert get_min_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_min_accel('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_max_speed(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the max speed of the driver
    :param name: name of profile
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type name: str
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the max speed that the driver is comfortable with
    """
    driver = DriverProfile(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_max_speed()


def test_get_max_speed():
    """
    Test function for get_max_speed function
    :return: Tests pass if max speed is returned properly, false if otherwise.
    """

    assert get_max_speed('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 75.0
    assert get_max_speed('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 1.2
    assert get_max_speed('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.4
    assert get_max_speed('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 25.2
    assert get_max_speed('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 2.2
    assert get_max_speed('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_max_speed('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_accel_time(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the acceleration time of the driver
    :param name: name of profile
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type name: str
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the amount of time it takes to accelerate to desired speed
    """
    driver = DriverProfile(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_accel_time()


def test_get_accel_time():
    """
    Test function for get_accel_time function
    :return: Tests pass if acceleration time is returned properly, false if otherwise.
    """

    assert get_accel_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) == 5.4
    assert get_accel_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 1.2
    assert get_accel_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 3.4
    assert get_accel_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 25.2
    assert get_accel_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 2.2
    assert get_accel_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 75.0
    assert get_accel_time('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 3.0


def get_update_time_ms(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the update time of the driver
    :param name: name of profile
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type name: str
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the interval in which the driver checks its surroundings
    """
    driver = DriverProfile(name, o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_update_time_ms()


def test_get_update_time_ms():
    """
    Test function for get_update_time_ms function
    :return: Tests pass if update time of driver is returned properly, false if otherwise.
    """

    assert get_update_time_ms('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) == 7.77
    assert get_update_time_ms('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 1.2
    assert get_update_time_ms('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 3.4
    assert get_update_time_ms('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 25.2
    assert get_update_time_ms('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 2.2
    assert get_update_time_ms('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 75.0
    assert get_update_time_ms('test', 1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 5.4


def update_over_braking_factor(driver, obf):
    """
    Updates the over braking factor of the driver
    :param driver: driver
    :param obf: new over braking factor
    :type driver: DriverProfile
    :return: updated driver profile
    """
    return driver.update_over_breaking_factor(obf)


def test_update_over_braking_factor():
    """
    Tests the update_over_braking_factor method
    :return: Tests if cases pass
    """
    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)

    assert default_driver.get_over_braking_factor() == 8

    update_over_braking_factor(default_driver, 15)

    assert default_driver.get_over_braking_factor() == 15


def update_following_time(driver, ft):
    """
    Updates the following time of the driver
    :param driver: driver
    :param ft: following time
    :type driver: DriverProfile
    :return: updated driver profile
    """
    return driver.update_following_time(ft)


def test_update_following_time():
    """
    Tests the update_following_time method
    :return: Tests if cases pass
    """
    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)

    assert default_driver.get_following_time() == 2

    update_following_time(default_driver, 5)

    assert default_driver.get_following_time() == 5


def update_max_accel(driver, ma):
    """
    Updates the max accel of the driver
    :param driver: driver
    :param ma: new max accel
    :type driver: DriverProfile
    :return: updated driver profile
    """
    return driver.update_max_accel(ma)


def test_update_max_accel():
    """
    Tests the update_max_accel method
    :return: Tests if cases pass
    """
    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)

    assert default_driver.get_max_accel() == 2

    update_max_accel(default_driver, 7)

    assert default_driver.get_max_accel() == 7


def update_min_accel(driver, min_a):
    """
    Updates the min accel of the driver
    :param driver: driver
    :param min_a: min accel
    :type driver: DriverProfile
    :return: updated driver profile
    """
    return driver.update_min_accel(min_a)


def test_update_min_accel():
    """
    Tests the update_min_accel method
    :return: Tests if cases pass
    """
    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)

    assert default_driver.get_min_accel() == 0

    update_min_accel(default_driver, 3)

    assert default_driver.get_min_accel() == 3


def update_max_speed(driver, speed):
    """
    Updates the max speed of the driver
    :param driver: driver
    :param speed: new max speed
    :type driver: DriverProfile
    :return: updated driver profile
    """
    return driver.update_max_speed(speed)


def test_update_max_speed():
    """
    Tests the update_max_speed method
    :return: Tests if cases pass
    """
    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)

    assert default_driver.get_max_speed() == 30

    update_max_speed(default_driver, 60)

    assert default_driver.get_max_speed() == 60


def update_accel_time(driver, at):
    """
    Updates the accel time of the driver
    :param driver: driver
    :param at: new accel time
    :type driver: DriverProfile
    :return: updated driver profile
    """
    return driver.update_accel_time(at)


def test_update_accel_time():
    """
    Tests the update_accel_time method
    :return: Tests if cases pass
    """
    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)

    assert default_driver.get_accel_time() == 3

    update_accel_time(default_driver, 9)

    assert default_driver.get_accel_time() == 9


def update_update_time_ms(driver, utm):
    """
    Updates the update time of the driver
    :param driver: driver
    :param utm: new update time
    :type driver: DriverProfile
    :return: updated driver profile
    """
    return driver.update_update_time_ms(utm)


def test_update_update_time_ms():
    """
    Tests the update_update_time_ms method
    :return: Tests if cases pass
    """
    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)

    assert default_driver.get_update_time_ms() == 1

    update_update_time_ms(default_driver, 4)

    assert default_driver.get_update_time_ms() == 4


def update_driver_profile_name(driver, name):
    """
    Updates the name of the driver
    :param driver: driver
    :param name: new name
    :type driver: DriverProfile
    :return: updated driver profile
    """
    return driver.update_driver_profile_name(name)


def test_update_driver_profile_name():
    """
    Tests the update_driver_profile_name method
    :return: Tests if cases pass
    """
    default_driver = DriverProfile("Default", 8, 2, 2, 0, 30, 3, 1)

    assert default_driver.get_driver_profile_name() == "Default"

    update_driver_profile_name(default_driver, "updatedname")

    assert default_driver.get_driver_profile_name() == "updatedname"