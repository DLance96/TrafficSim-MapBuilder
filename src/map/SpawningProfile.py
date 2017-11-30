import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.DriverProfile import DriverProfile
from src.map.VehicleProfile import VehicleProfile


class SpawningProfile:

    def __init__(self, profile_name, driver_profile, vehicle_profile):
        self.profile_name = profile_name
        self.driver_profile = driver_profile
        self.vehicle_profile = vehicle_profile

    def get_spawning_profile_name(self):
        return self.profile_name

    def get_driver_profile(self):
        return self.driver_profile

    def get_vehicle_profile(self):
        return self.vehicle_profile

    def update_spawning_profile_name(self, new_name):
        self.profile_name = new_name

    def update_driver_profile(self, new_driver_profile):
        self.driver_profile = new_driver_profile

    def update_vehicle_profile(self, new_vehicle_profile):
        self.vehicle_profile = new_vehicle_profile


