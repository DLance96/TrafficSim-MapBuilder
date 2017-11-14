import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from src.map.DriverProfile import DriverProfile


def get_over_braking_factor(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the over braking factor of the driver
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the overbraking factor of the driver
    """

    driver = DriverProfile(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_over_braking_factor()


def test_get_over_braking_factor():
    """
    Test function for get_over_braking_factor function
    :return: Tests pass if over braking factor is returned properly, false if otherwise.
    """

    assert get_over_braking_factor(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 1.2
    assert get_over_braking_factor(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.4
    assert get_over_braking_factor(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 25.2
    assert get_over_braking_factor(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 2.2
    assert get_over_braking_factor(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 75.0
    assert get_over_braking_factor(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_over_braking_factor(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_following_time(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the following time of the driver
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the following time of the driver
    """
    driver = DriverProfile(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_following_time()


def test_get_following_time():
    """
    Test function for get_following_time function
    :return: Tests pass if following time is returned properly, false if otherwise.
    """

    assert get_following_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 3.4
    assert get_following_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 1.2
    assert get_following_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 25.2
    assert get_following_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 2.2
    assert get_following_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 75.0
    assert get_following_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_following_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_max_accel(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the max acceleration of the driver
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the max acceleration that the driver is comfortable with
    """
    driver = DriverProfile(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_max_accel()


def test_get_max_accel():
    """
    Test function for get_max_accel function
    :return: Tests pass if maximum acceleration is returned properly, false if otherwise.
    """

    assert get_max_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 25.2
    assert get_max_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 1.2
    assert get_max_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.4
    assert get_max_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 2.2
    assert get_max_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 75.0
    assert get_max_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_max_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_min_accel(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the min acceleration of the driver
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the min acceleration that the driver is comfortable with
    """
    driver = DriverProfile(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_min_accel()


def test_get_min_accel():
    """
    Test function for get_min_accel function
    :return: Tests pass if minimum acceleration is returned properly, false if otherwise.
    """

    assert get_min_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 2.2
    assert get_min_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 1.2
    assert get_min_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.4
    assert get_min_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 25.2
    assert get_min_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 75.0
    assert get_min_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_min_accel(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_max_speed(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the max speed of the driver
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the max speed that the driver is comfortable with
    """
    driver = DriverProfile(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_max_speed()


def test_get_max_speed():
    """
    Test function for get_max_speed function
    :return: Tests pass if max speed is returned properly, false if otherwise.
    """

    assert get_max_speed(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) == 75.0
    assert get_max_speed(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 1.2
    assert get_max_speed(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.4
    assert get_max_speed(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 25.2
    assert get_max_speed(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 2.2
    assert get_max_speed(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 5.0
    assert get_max_speed(1.2, 3.4, 25.2, 2.2, 75.0, 5.0, 3.0) != 3.0


def get_accel_time(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the acceleration time of the driver
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the amount of time it takes to accelerate to desired speed
    """
    driver = DriverProfile(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_accel_time()


def test_get_accel_time():
    """
    Test function for get_accel_time function
    :return: Tests pass if acceleration time is returned properly, false if otherwise.
    """

    assert get_accel_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) == 5.4
    assert get_accel_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 1.2
    assert get_accel_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 3.4
    assert get_accel_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 25.2
    assert get_accel_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 2.2
    assert get_accel_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 75.0
    assert get_accel_time(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 3.0) != 3.0


def get_update_time_ms(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms):
    """
    Function returns the update time of the driver
    :param o_b_f: over braking factor of the driver
    :param f_t: following time of the driver
    :param max_a: max acceleration that the driver is comfortable with
    :param min_a: min acceleration that the driver is comfortable with
    :param max_s: max speed that the driver is comfortable with
    :param a_t: the amount of time it takes for the driver to accelerate to a desired speed
    :param u_t_ms: intervals in which the driver checks its surroundings
    :type o_b_f: float
    :type f_t: float
    :type max_a: float
    :type min_a: float
    :type max_s: float
    :type a_t: float
    :type u_t_ms: float
    :return: the interval in which the driver checks its surroundings
    """
    driver = DriverProfile(o_b_f, f_t, max_a, min_a, max_s, a_t, u_t_ms)
    return driver.get_update_time_ms()


def test_get_update_time_ms():
    """
    Test function for get_update_time_ms function
    :return: Tests pass if update time of driver is returned properly, false if otherwise.
    """

    assert get_update_time_ms(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) == 7.77
    assert get_update_time_ms(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 1.2
    assert get_update_time_ms(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 3.4
    assert get_update_time_ms(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 25.2
    assert get_update_time_ms(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 2.2
    assert get_update_time_ms(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 75.0
    assert get_update_time_ms(1.2, 3.4, 25.2, 2.2, 75.0, 5.4, 7.77) != 5.4