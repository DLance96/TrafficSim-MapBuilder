from src.map.map_object import MapObject
from src.exceptions import MaxConnectionsException
from src.map.constants import *


class Intersection(MapObject):
    def __init__(self):
        """
        Establish a intersection for the TrafficMap
        """
        MapObject.__init__(self)
        self.spawning_profiles = []

    def add_spawning_profile(self, profile):
        """
        Adds a spawning profile to the intersection
        :param profile: profile to be added
        """
        self.spawning_profiles.append(profile)

    def get_spawning_profiles(self):
        """
        :return: all the spawning profiles of a intersection
        """
        return self.spawning_profiles

    def remove_spawning_profile(self, profile):
        """
        Removes spawning profile from intersection
        :param profile: profile to remove
        """
        self.spawning_profiles.remove(profile)


class Intersection2(Intersection):
    def __init__(self):
        """
        Creates an empty 4-way intersection that can be treated as a 3-way when needed
        """
        Intersection.__init__(self)

    def add_connection(self, map_piece, angle):
        """
        Allows Intersections to limit the number of connections made through it
        :param map_piece: map_piece to add to the connection
        :param angle: where to add the new connection
        """
        # TODO set some limit on the number of roads entering an intersection
        Intersection.add_connection(self, map_piece, angle)


# TODO
class Turn(Intersection):
    def __init__(self, radius, lanes):
        """
        Creating a turn
        :param radius: radius of the turn
        :param lanes: how many lanes are in the turn
        """
        Intersection.__init__(self)
        self.lanes = lanes
        self.radius = radius

    def add_connection(self, map_piece, angle):
        """
        Adds connections to the turn, angles are based on the angle from the center of the radius
        :param map_piece:
        :param angle:
        :return:
        """
        if len(self.connections.values()) == TURN_CONNECTION_LIMIT:
            raise MaxConnectionsException(self, TURN_CONNECTION_LIMIT)
        else:
            Intersection.add_connection(map_piece, angle)


# TODO
class LaneAdjustment(Intersection):
    def __init__(self, enter_direction):
        """
        Creates a intersection that shifts a road up or down in lanes
        :param enter_direction: a direction to orient the LaneAdjustment
        """
        directions = [enter_direction, enter_direction]
        Intersection.__init__(self, directions)
        self.lanes = {
            directions[0]: 0,
            directions[1]: 0,
        }

    def add_path(self, path, direction):
        """
        Adds path while also keeping track of lane counts
        :param path: path to add
        :param direction: where to add path
        :return: raise error according to intersection.add_path
        """
        Intersection.add_path(self, path, direction)
        self.lanes[direction] = path.get_lanes()

    def remove_path(self, direction):
        """
        Removes path while keeping track of lane counts
        :param direction: which path to remove
        :return: raise error according to intersection.remove_path
        """
        Intersection.remove_path(self, direction)
        self.lanes[direction] = 0


class Portal(Intersection):
    def __init__(self):
        """
        A intersection for exclusively spawning drivers according to spawning_profiles
        """
        Intersection.__init__(self)

    def add_connection(self, map_piece, angle):
        """
        Adds connection recognizing the PORTAL_CONNECTION_LIMIT
        :param map_piece: the MapObject needed to add
        :param angle: where to add the MapObject
        """
        if len(self.connections.keys()) == PORTAL_CONNECTION_LIMIT:
            raise MaxConnectionsException(self, PORTAL_CONNECTION_LIMIT)
        else:
            Intersection.__init__(map_piece, angle)
