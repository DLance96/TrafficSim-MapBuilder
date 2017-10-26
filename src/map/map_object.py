from src.utils import get_opposite_angle
from src.exceptions import AngleAlreadyInUseException, NotInitializedSetException


class MapObject(object):
    def __init__(self):
        """
        MapObjects are the parts of the map that when combined make up the whole road map. The conmection is a dictonary
        of angles bound to MapObjects which represent how the piece is connected to other parts
        """
        self.connections = dict()

    def add_connection(self, map_object, angle):
        """
        Adds connection to the connection dict accordingly
        :param map_object: piece to be added
        :param angle: the angle that the new piece is connected in relation to the current piece
        :return: raises error if there is alreaady a piece at a chosen degree
        """
        if angle not in self.connections.keys() and not map_object.has_connection(get_opposite_angle(angle)):
            map_object.add_connection(self, get_opposite_angle(angle))
            self.connections[angle] = map_object
        else:
            if self.connections[angle] == map_object:
                return
            else:
                raise AngleAlreadyInUseException(self, angle)

    def remove_connection(self, angle):
        """
        Removes map piece from the connection dict
        :param angle: angle to remove piece from
        """
        if angle in self.connections.keys():
            map_object = self.connections[angle]
            del self.connections[angle]
            map_object.remove_connection(get_opposite_angle(angle))

    def get_connection(self, angle):
        """
        Gets map piece from the given angle
        :param angle: angle where the connection is located
        :return: the map piece corresponding to the given angle
        """
        if angle in self.connections.keys():
            return self.connections[angle]
        else:
            raise NotInitializedSetException(self, angle)

    def has_connection(self, angle):
        """
        Check if angle is already in use
        :param angle: which angle to check
        :return: Boolean depending on the existence of the map piece
        """
        # TODO how close should connection be with regards to angles
        if angle in self.connections.keys():
            return True
        else:
            return False
