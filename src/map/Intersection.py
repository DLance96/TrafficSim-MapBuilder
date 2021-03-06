import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Coordinates import Coordinates
from src.map.SpawningProfile import SpawningProfile


class Intersection(object):
    """
    This class represents an intersection object in the MapBuilder section of our application.
    An intersection is represented in our implementation by a circle, where roads
    can connect to it at any point along its circumference.

    """

    default_yellow_length = 4000

    def __init__(self, central_point, radius, speed_limit):
        """
        Establishes an intersection object

        :param central_point: center point of the intersection circle
        :param radius: radius of the intersection circle
        :param speed_limit: speed limit

        :type central_point: Coordinates
        :type radius: float
        :type speed_limit: int
        """
        self.center = central_point
        self.radius = radius
        self.speed_limit = speed_limit
        self.connections = []
        self.spawn_profiles = []
        self.cycle_names = []
        self.green_cycle_roads = []
        self.green_cycle_times = []
        self.yellow_light_length = self.default_yellow_length  # time in milliseconds

    # need to create another constructor to handle a central point and its connecting object (CHECK IF THAT IS TRUE)
    def add_cycle(self, name, roads, time):
        self.cycle_names.append(name)
        self.green_cycle_roads.append(roads)
        self.green_cycle_times.append(time)

    def get_frequency(self):
        return 10000

    def remove_cycle(self, name):
        i = 0

        for cycle_name in self.cycle_names:
            if name == cycle_name:
                break
            i = i + 1

        self.cycle_names.pop(i)
        self.green_cycle_roads.pop(i)
        self.green_cycle_times.pop(i)

    def reset_light(self):
        self.cycle_names = []
        self.green_cycle_roads = []
        self.green_cycle_times = []
        self.yellow_light_length = self.default_yellow_length

    def set_yellow_length(self, length):
        self.yellow_light_length = length

    def add_spawning_profile(self, spawning_profile):
        """
        Adds a spawning profile to the intersection
        :param spawning_profile: Spawning profile to be added to intersection
        :type spawning_profile: SpawningProfile
        :return: Updated spawning profile list of intersection
        """
        if spawning_profile is not None:
            self.spawn_profiles.append(spawning_profile)

    def remove_spawning_profile(self, deleted_profile):
        """
        Removes a spawning profile from an intersection
        :param deleted_profile: Spawning profile to be removed from intersection
        :type deleted_profile: SpawningProfile
        :return: Updated spawning profile list without removed spawning profile
        """

        is_in_list = False

        if deleted_profile is not None:
            for profile in self.spawn_profiles:
                if profile.get_spawning_profile_name() == deleted_profile.get_spawning_profile_name():
                    is_in_list = True
                    break

            if is_in_list:
                self.spawn_profiles.remove(deleted_profile)
            else:
                print('Profile not found in list!')

    def get_spawning_profile_list(self):
        """
        Get the spawning profiles attached to this intersection
        :return: spawning profiles attached to this intersection
        """
        return self.spawn_profiles

    def get_speed_limit(self):
        """
        Get the speed limit of this intersection
        :return: speed limit of this intersection
        """
        return self.speed_limit

    def update_speed_limit(self, new_speed):
        """
        Update the speed limit of this intersection
        :param new_speed: new speed limit
        :type new_speed: int
        :return: None
        """
        self.speed_limit = new_speed

    def add_connection(self, angle, distance, in_lanes, out_lanes, speed_limit, name):
        """
        Currently adds a road to the intersection
        :param angle: angle that the road protrudes from the intersection relative to the intersection's origin
        :param distance: length of the road
        :param in_lanes: number of incoming lanes that the road contains
        :param out_lanes: number of outgoing lanes that the road contains

        :type name: str
        :type angle: float
        :type distance: float
        :type in_lanes: int
        :type out_lanes: int

        :return: returns road object for added connection
        """

        start_x = self.center.get_x() + (self.radius * math.sin(angle))
        start_y = self.center.get_y() + (self.radius * math.cos(angle))

        start_coord = Coordinates(start_x, start_y)

        end_x = self.center.get_x() + ((self.radius + distance) * math.sin(angle))
        end_y = self.center.get_y() + ((self.radius + distance) * math.cos(angle))

        end_coord = Coordinates(end_x, end_y)

        road = Road(start_coord, end_coord, distance, out_lanes, in_lanes, angle, speed_limit, name)
        road.add_start_connection(self)

        self.connections.append(road)

        return road

    def add_incoming_connection(self, road):
        """
        Adds an incoming road
        :param road: road that is incoming
        :type road: Road
        :return: the road that was input
        """
        self.connections.append(road)

        return road

    def add_outgoing_connection(self, road):
        """
        Adds an outgoing road
        :param road: road that is outgoing
        :type road: Road
        :return: the road that was input
        """
        self.connections.append(road)

        return road

    def get_center(self):
        """
        :return: center point of the intersection circle
        """
        return self.center

    def get_radius(self):
        """
        :return: radius of the intersection circle
        """
        return self.radius

    def get_connections(self):
        """
        :return: list of map objects that are connected to this intersection
        """

        return self.connections

    def update_radius(self, new_radius):
        """
        Updates the radius of the intersection circle

        :param new_radius: new radius of the intersection circle
        :type new_radius: float

        :return: None
        """
        self.radius = new_radius

    def is_on_intersection(self, coordinate):
        """
        Determines if a given coordinate point is within the boundaries of the current intersection
        :param coordinate: coordinate point that will be tested for being within intersection boundaries
        :type coordinate: coordinates.coordinates
        :return: returns true if given coordinate is within the boundaries of the intersection. Otherwise, returns false
        """
        delta_x = self.center.get_x() - coordinate.x
        delta_y = self.center.get_y() - coordinate.y

        x_squared = delta_x * delta_x
        y_squared = delta_y * delta_y

        distance = math.sqrt(x_squared + y_squared)

        if self.radius >= distance:
            return True
        return False
