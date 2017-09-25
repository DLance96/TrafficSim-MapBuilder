from src.utils import Direction
from src.exceptions import NotInitializedSetException, DirectionUnavailableException


class Path(object):

    def __init__(self, lanes, path_direction):
        """

        :param lanes:
        :param path_direction:
        """
        self.lanes = lanes
        self.nodes = [None, None, None, None]
        self.nodes_directions = [path_direction, Direction.get_opposite(path_direction)]

    def add_node(self, node, direction):
        """

        :param node:
        :param direction:
        :return:
        """
        if direction in self.nodes_directions:
            self.nodes[direction.value] = node
        else:
            raise DirectionUnavailableException(self, direction)

    def get_node(self, direction):
        """

        :param direction:
        :return:
        """
        if direction in self.nodes_directions:
            if self.nodes[direction.value] is not None:
                return self.nodes[direction.value]
            else:
                raise NotInitializedSetException(self, direction)
        else:
            raise DirectionUnavailableException(self, direction)

    def remove_node(self, direction):
        """

        :param direction:
        :return:
        """
        if direction in self.nodes_directions:
            self.nodes[direction.value] = None
        else:
            raise DirectionUnavailableException(self, direction)

    def get_lanes(self):
        return self.lanes


class Road(Path):

    def __init__(self, length, speed_limit, enter_direction):
        """
        Creates a road
        :param length: length of the road
        :param speed_limit: speed limit on the road
        :param enter_direction: where the
        """
        Path.__init__(self, enter_direction)
        self.length = length
        self.speed_limit = speed_limit
