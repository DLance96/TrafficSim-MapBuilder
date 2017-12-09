import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.DriverProfile import DriverProfile
from src.map.VehicleProfile import VehicleProfile


class SpawningProfile:

    """
    This class represents a spawning profile to be used in the MapBuilder. Users can create spawning profiles and attach
    them to intersections. While the simulation is running, said intersections will spawn vehicles based off of the
    information from the attached spawning profile.
    """

    def __init__(self, profile_name, driver_profile, vehicle_profile):
        """
        Establishes a spawning profile
        :param profile_name: Name of the spawning profile
        :param driver_profile: Driver of the vehicle to be spawned
        :param vehicle_profile: Vehicle to be spawned

        :type profile_name: str
        :type driver_profile: DriverProfile
        :type vehicle_profile: VehicleProfile
        """
        self.profile_name = profile_name
        self.driver_profile = driver_profile
        self.vehicle_profile = vehicle_profile

    def get_spawning_profile_name(self):
        """
        :return: the name of the spawning profile
        """
        return self.profile_name

    def get_driver_profile(self):
        """
        :return: the name of the driver profile
        """
        return self.driver_profile

    def get_vehicle_profile(self):
        """
        :return: the name of the vehicle profile
        """
        return self.vehicle_profile

    def update_spawning_profile_name(self, new_name):
        """
        Updates the name of the spawning profile
        :param new_name: new name for the spawning profile
        :return: updated spawning profile
        """
        self.profile_name = new_name

    def update_driver_profile(self, new_driver_profile):
        """
        Updates the driver profile of the spawning profile
        :param new_driver_profile: new driver profile for the spawning profile
        :return: updated spawning profile
        """
        self.driver_profile = new_driver_profile

    def update_vehicle_profile(self, new_vehicle_profile):
        """
        Updates the vehicle profile of the spawning profile
        :param new_vehicle_profile: new name for the spawning profile
        :return: updated spawning profile
        """
        self.vehicle_profile = new_vehicle_profile


