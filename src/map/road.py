from src.map.map_object import MapObject
from src.utils import get_opposite_angle
from src.exceptions import MaxConnectionsException, MismatchAngleException
from src.map.constants import ROAD_CONNECTION_LIMIT


class Road(MapObject):

    def __init__(self, length, speed_limit, angle):
        """
        Create a road MapObject
        :param length: how long the road is
        :param speed_limit: sets the speed limit on the road
        :param angle: sets the orientation of the road
        """
        MapObject.__init__(self)
        self.length = length
        self.speed_limit = speed_limit
        self.angle = angle

    def add_connection(self, map_piece, angle):
        """
        Adds a connection to this road, if there are prior connections the new map pieces may not be added to keep the
        road straight
        :param map_piece: piece to connect
        :param angle: where to connect the road
        :return: raises an error if you already have added all the connection or if the connection does to maintain the
        straight nature of the road
        """
        if len(self.connections.keys()) == 0:
            MapObject.add_connection(self, map_piece, angle)
            self.angle = angle
        elif len(self.connections.keys()) == ROAD_CONNECTION_LIMIT - 1:
            if self.connections.keys()[0] == get_opposite_angle(angle):
                MapObject.add_connection(self, map_piece, angle)
            else:
                raise MismatchAngleException()
        elif len(self.connections.keys()) == ROAD_CONNECTION_LIMIT:
            raise MaxConnectionsException(self, ROAD_CONNECTION_LIMIT)
        else:
            raise NotImplementedError()
