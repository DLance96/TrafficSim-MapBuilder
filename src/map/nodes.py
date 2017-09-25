from src.map.paths import Path
from src.exceptions import NotInitializedSetException, DirectionUnavailableException
from src.utils import Direction


class Node(object):

    def __init__(self, path_directions):
        """
        Establish a node for the TrafficMap
        :param path_directions: directions that can enter or exit a given node
        """
        self.paths = [None, None, None, None]
        self.path_directions = path_directions

    def add_path(self, path: Path, direction: Direction):
        """
        Add a path reference for the endpoints of a node
        :param path: path reference
        :param direction: where the path is in relation to the node
        :return: raises exception if a path is added when it is not a valid location
        """
        if direction in self.path_directions:
            self.paths[direction.value] = path
        else:
            raise DirectionUnavailableException(self, direction)

    def get_path(self, direction):
        """
        Get a path reference if it exists
        :param direction: which direction to check for path
        :return: path of given direction
        """
        if direction in self.path_directions:
            if self.paths[direction.value] is not None:
                return self.paths[direction.value]
            else:
                raise NotInitializedSetException(self, direction)
        else:
            raise DirectionUnavailableException(self, direction)

    def remove_path(self, direction):
        """
        Removes path from node
        :param direction: direction from where the node should be removed
        :return: will raise an error if the given direction is not a valid direction on this node
        """
        if direction in self.path_directions:
            self.paths[direction.value] = None
        else:
            raise DirectionUnavailableException(self, direction)


class Intersection(Node):

    def __init__(self):
        """
        Creates an empty 4-way intersection that can be treated as a 3-way when needed
        """
        directions = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        Node.__init__(self, directions)


class Turn(Node):

    def __init__(self, enter_direction, exit_direction, radius, lanes):
        """
        Creates a turn node for the map
        :param enter_direction: the direction that the starting path comes from
        :param exit_direction: the direction that the turn will face
        :param radius: radius of the turn
        :param lanes: number of lanes in the turn
        """
        directions = [enter_direction, exit_direction]
        Node.__init__(self, directions)
        self.lanes = lanes
        self.radius = radius


class LaneAdjustment(Node):

    def __init__(self, enter_direction):
        """
        Creates a node that shifts a road up or down in lanes
        :param enter_direction: a direction to orient the laneadjustment
        """
        directions = [enter_direction, Direction.get_opposite(enter_direction)]
        Node.__init__(self, directions)
        self.lanes = {
            directions[0]: 0,
            directions[1]: 0,
        }

    def add_path(self, path, direction):
        """
        Adds path while also keeping track of lane counts
        :param path: path to add
        :param direction: where to add path
        :return: raise error according to Node.add_path
        """
        Node.add_path(self, path, direction)
        self.lanes[direction] = path.get_lanes()

    def remove_path(self, direction):
        """
        Removes path while keeping track of lane counts
        :param direction: which path to remove
        :return: raise error according to Node.remove_path
        """
        Node.remove_path(self, direction)
        self.lanes[direction] = 0
