import sys
import os
import math

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Coordinates import Coordinates


class Intersection(object):
    """
    This class represents an intersection object in the MapBuilder section of our application.
    An intersection is represented in our implementation by a circle, where roads
    can connect to it at any point along its circumference.

    """

    def __init__(self, central_point, radius, speed_limit):
        """
        Establishes an intersection object

        :param central_point: center point of the intersection circle
        :param radius: radius of the intersection circle

        :type central_point: Coordinates
        :type radius: float
        """
        self.center = central_point
        self.radius = radius
        self.speed_limit = speed_limit
        self.connections = []
        self.spawn_profiles = []

    # need to create another constructor to handle a central point and its connecting object (CHECK IF THAT IS TRUE)

    def add_spawning_profile(self, spawning_profile):
        if spawning_profile is not None:
            self.spawn_profiles.append(spawning_profile)

    def remove_spawning_profile(self, deleted_profile):

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

    def get_speed_limit(self):
        return self.speed_limit

    def update_speed_limit(self, new_speed):
        self.speed_limit = new_speed

    def add_connection(self, angle, distance, in_lanes, out_lanes, speed_limit):
        """
        Currently adds a road to the intersection
        :param angle: angle that the road protrudes from the intersection relative to the intersection's origin
        :param distance: length of the road
        :param in_lanes: number of incoming lanes that the road contains
        :param out_lanes: number of outgoing lanes that the road contains

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

        road = Road(start_coord, end_coord, distance, out_lanes, in_lanes, angle, speed_limit)
        road.add_start_connection(self)

        self.connections.append(road)

        return road

    def add_incoming_connection(self, road):
        """
        Adds an incoming road
        :param road: road that is incoming
        :return: the road that was input
        """
        self.connections.append(road)

        return road

    def add_outgoing_connection(self, road):
        """
        Adds an outgoing road
        :param road: road that is outgoing
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

    def update_center(self, new_center):
        """
        Updates the center point of the intersection circle

        :param new_center: new center point of the intersection circle
        :type new_center: Coordinates

        :return: None
        """
        self.center = new_center

    def update_radius(self, new_radius):
        """
        Updates the radius of the intersection circle

        :param new_radius: new radius of the intersection circle
        :type new_radius: float

        :return: None
        """
        self.radius = new_radius

    def update_connections(self, new_connections):
        """
        Updates the list of outgoings connections for the intersection

        :param new_connections: new list of connections for the intersection
        :type new_connections: list consisting of map objects

        :return: None
        """
        self.connections = new_connections

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
