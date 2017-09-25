from src.utils import Direction
from src.exceptions import NotInitializedSetException, DirectionUnavailableException


class Path(object):

    def __init__(self, lanes, path_direction):
        """
        A path connects two nodes together
        :param lanes: number of lanes on the path
        :param path_direction: the orientation of the path i.e. North will make it NS, E will make it EW and so on
        """
        self.lanes = lanes
        self.nodes = [None, None, None, None]
        self.nodes_directions = [path_direction, Direction.get_opposite(path_direction)]

    def add_node(self, node, direction):
        """
        Adds end node of a path
        :param node: node to be added
        :param direction: where the node should be added
        :return: raise error if the direction was not intialized where the node should be added
        """
        if direction in self.nodes_directions:
            self.nodes[direction.value] = node
        else:
            raise DirectionUnavailableException(self, direction)

    def get_node(self, direction):
        """
        :param direction: which node to get
        :return: raise error if direction is not setup for this node or the node is None
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
        Remove node from path
        :param direction: which node to remove
        :return: raise error if direction is not valid
        """
        if direction in self.nodes_directions:
            self.nodes[direction.value] = None
        else:
            raise DirectionUnavailableException(self, direction)

    def get_lanes(self):
        """
        :return: number of lanes in a path
        """
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
