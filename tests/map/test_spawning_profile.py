import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from src.map.VehicleProfile import VehicleProfile
from src.map.DriverProfile import  DriverProfile


def get_spawning_profile_name(vehicle_profile, driver_profile):
    print('test')
